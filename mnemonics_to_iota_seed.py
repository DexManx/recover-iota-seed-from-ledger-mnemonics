# -*- coding: utf-8 -*-
from mnemonics_utils import MnemonicsToIotaSeed, InputRecoveryWords, InputPassphrase, InputLedgerStartIndex


# ===============================================================================
def RecoverSeed():
    print("\nWelcome to IOTA Ledger Nano seed recovery!")

    recovery_words = InputRecoveryWords()
    if recovery_words is None:
        return

    passphrase = InputPassphrase()
    if passphrase is None:
        return

    trinity_index = int(InputLedgerStartIndex() or 0)

    print("\nCalculating your IOTA seed...")
    iota_seed = MnemonicsToIotaSeed(recovery_words, passphrase, trinity_index)
    print("Seed: %s, Length: %d" % (iota_seed, len(iota_seed)))


# ===============================================================================
if __name__ == '__main__':
    RecoverSeed()
