# -*- coding: utf-8 -*-
import sys

from mnemonics_utils import MnemonicsToIotaSeed, InputRecoveryWords, InputPassphrase, InputLedgerStartIndex
from search_ledger_index_by_mnemonics_by_target_address import SearchLedgerIndexByTargetAddress


# ===============================================================================
def RecoverSeed():
    print("\nWelcome to IOTA Ledger Nano seed recovery!")

    recovery_words = ["zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo",
                      "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo"]

    passphrase = sys.argv[1]          # InputPassphrase()
    if passphrase is None:
        return

    # trinity_index = int(InputLedgerStartIndex() or 0)
    # print("\nCalculating your IOTA seed...")
    # iota_seed = MnemonicsToIotaSeed(recovery_words, passphrase, 1)
    # print("Seed: %s, Length: %d" % (iota_seed, len(iota_seed)))

    SearchLedgerIndexByTargetAddress(recovery_words, passphrase, 1, 1, 0, 0, 3,
                                     "AXWJBOBKCY9BXYELWRVAFUQYVLPRJIVADOSUPHEMDEF9YRXQYEO9OZXFTLVYDYITKKUQEOJIPRLAXXVXD")


# ===============================================================================
if __name__ == '__main__':
    RecoverSeed()
