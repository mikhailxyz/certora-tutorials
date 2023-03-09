### Unit test

- can be joined only when started
- cant be started before the start time
- can only be started within [start time, end time]
- end time has to be after start time

### Variable transition

### State transition

- valid state transitions:
  - uninitialized -> pending
  - pending -> started or canceled
  - started -> ended
  - canceled -> canceled

### Valid states

- uninitalized && 0 participants

### High Level Properties

- numbers of participants cant be decreased
