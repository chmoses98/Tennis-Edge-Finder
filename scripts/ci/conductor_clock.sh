# Loop budget for the self-chaining conductors (tennis-capture.yml, tennis-firstball.yml). Sourced, not run.
#
# Why this exists: both loops checked their END only at the TOP of a pass, measured END from the start of the
# loop step (not the job), and let the post-pass sleep run past END. The last pass therefore regularly carried a
# 340-minute loop to 350-360 minutes, and the job hit its 355-minute `timeout-minutes`: GitHub then killed it
# mid-pass and the run ended CANCELLED although the conductor had done exactly its job (37 of ~85 capture
# conductor runs in the 2026-09-11..10-02 history). A cancelled-by-timeout run is indistinguishable from a real
# hang, so the timeout stopped meaning anything.
#
# The rule here: END is the earlier of (loop start + MINUTES) and (job start + timeout - safety), a pass starts
# only if the LONGEST pass seen so far still fits before END, and the inter-pass sleep never crosses END. A pass
# that genuinely hangs still hits `timeout-minutes` and still ends the run (that is a real fault).
#
# All arguments are integer epoch seconds or minutes; no clock is read here, so the functions are deterministic
# (tests/test_conductor_ci.py drives them with fixed numbers).

# conductor_end LOOP_START MINUTES JOB_START JOB_TIMEOUT_MIN SAFETY_MIN -> prints END (epoch seconds)
conductor_end() {
  local soft=$(( $1 + $2 * 60 ))
  local hard=$(( $3 + ($4 - $5) * 60 ))
  if [ "$soft" -lt "$hard" ]; then echo "$soft"; else echo "$hard"; fi
}

# conductor_should_start NOW END LONGEST_PASS_SECONDS -> exit 0 when another pass fits before END
conductor_should_start() {
  [ $(( $1 + $3 )) -lt "$2" ]
}

# conductor_sleep NOW END INTERVAL ELAPSED -> prints seconds to sleep (never past END, never negative)
conductor_sleep() {
  local s=$(( $3 - $4 ))
  local left=$(( $2 - $1 ))
  if [ "$left" -lt "$s" ]; then s=$left; fi
  if [ "$s" -lt 0 ]; then s=0; fi
  echo "$s"
}
