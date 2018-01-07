#include <signal.h>

namespace flowthrone {

static volatile bool has_sigint_occurred = false;

bool HasSigIntOccurredSinceLastCall() {
  bool occurred = has_sigint_occurred;
  has_sigint_occurred = false;
  return occurred;
}

void SetSigIntOccurredVariable(int signum) { has_sigint_occurred = true; }

void InstallSigIntHandler() { signal(SIGINT, SetSigIntOccurredVariable); }

}  // namespace flowthrone
