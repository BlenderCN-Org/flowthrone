#pragma once

#include <signal.h>

namespace flowthrone {

// Installs the signal handler for SIGINT. The user can query whether SIGINT
// has occurred by calling HasSigIntOccurredSinceLastCall.
// The intended use of these functions is for cleanly exiting an
// expensive/long/infinite loops; something like:
//
// InstallSigIntHandler();
// while (true) {
//   if (HasSigIntOccurredSinceLastCall()) {
//     break;
//   }
//   // do lots of work..
// }
//
// Note that if you install this handler, then you will obviously lose the
// ability to (immediately) stop the program with Ctrl+C.
void InstallSigIntHandler();
bool HasSigIntOccurredSinceLastCall();

}  // namespace flowthrone
