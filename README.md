# chg-autopilot-sandbox

A throwaway repository for testing Code Health Guardian's Autopilot merge mode. The code is a toy and contains deliberately planted bugs. Nothing here is meant to be used.

`ci.yml` fails on a push to `main` while the repository variable `FORCE_RED_MAIN` is `1`. Pull request checks are unaffected. This is how the test turns the default branch red after a merge.
