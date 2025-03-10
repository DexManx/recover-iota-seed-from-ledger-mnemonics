# -*- coding: utf-8 -*-
import sys, mnemonic, bip32utils
from six.moves import input
from iota.crypto.kerl import Kerl, conv


# ===============================================================================
def MnemonicsToIotaSeed(recovery_words,
                        passphrase='',
                        bip44_account=0x00000000,
                        bip44_page_index=0x00000000):
    """Recover an IOTA seed from the ledger Nano S recovery phrase

    Keyword arguments:
    recovery_words -- a list of 24 words (your ledger recovery phrase)
    passphrase -- a string containing the passphrase (only if set in ledger, not your pin number!)
    bip44_account -- an integer containing BIP44 path 'Account'
    bip44_page_index -- an integer containing BIP44 path 'Page index'
    """

    master_seed = mnemonic.Mnemonic.to_seed(mnemonic=' '.join(recovery_words), passphrase=passphrase)
    bip32_root_key = bip32utils.BIP32Key.fromEntropy(master_seed)

    bip44_purpose_key = bip32_root_key.ChildKey(0x8000002C)  # Purpose
    bip44_coin_type_key = bip44_purpose_key.ChildKey(0x8000107A)  # CoinType
    bip44_account_key = bip44_coin_type_key.ChildKey(0x80000000 + bip44_account)  # Account
    bip44_page_index_key = bip44_account_key.ChildKey(0x80000000 + bip44_page_index)  # Page index

    if (sys.version_info.major >= 3):
        priv_key = bytearray(bip44_page_index_key.PrivateKey())
        chain_code = bytearray(bip44_page_index_key.C)
    else:
        priv_key = bytearray.fromhex(bip44_page_index_key.PrivateKey().encode('hex'))
        chain_code = bytearray.fromhex(bip44_page_index_key.C.encode('hex'))

    trits_out = []

    kerl = Kerl()
    kerl.k.update(priv_key[0:32] + chain_code[0:16] + priv_key[16:32] + chain_code[0:32])
    kerl.squeeze(trits_out)

    iota_seed = conv.trits_to_trytes(trits_out)

    return iota_seed


# ===============================================================================
def InputRecoveryWords():
    print("\nPlease enter your Ledger Nano S recovery phrase now:")

    m = mnemonic.Mnemonic(language='english')

    recovery_words = ["zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo",
                      "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo", "zoo"]

    # for i in range(24):
    #     while True:
    #         try:
    #             word = input("   word #%d: " % (i+1))
    #         except KeyboardInterrupt:
    #             return None
    #
    #         if word == '':
    #             print("\nERROR: word #%d was empty!" % (i+1))
    #             continue
    #
    #         try:
    #             m.wordlist.index(word)
    #         except ValueError:
    #             print("\nERROR: word '%s' is not in the BIP44 words list!" % (word))
    #             continue
    #
    #         recovery_words.append(word)
    #         break

    return recovery_words


# ===============================================================================
def InputPassphrase():
    print("\nPlease enter your Ledger Nano S passphrase now (only if set in the ledger, not your pin number!):")

    try:
        return input("   Ledger passphrase: ")
    except KeyboardInterrupt:
        return None


# ===============================================================================
def InputLedgerStartIndex():
    print("\nPlease enter ledger account index (Trinity default 0):")

    try:
        return input("   Ledger account index: ")
    except KeyboardInterrupt:
        return None


# ===============================================================================
def InputLedgerEndIndex():
    print("\nPlease enter ledger end index (Trinity default 0):")

    try:
        return input("   Ledger end index: ")
    except KeyboardInterrupt:
        return None


# ===============================================================================
def InputLedgerStartPage():
    print("\nPlease enter ledger start page (Trinity default 0):")

    try:
        return input("   Ledger start page: ")
    except KeyboardInterrupt:
        return None


# ===============================================================================
def InputLedgerEndPage():
    print("\nPlease enter ledger end page (Trinity default 0):")

    try:
        return input("   Ledger end page: ")
    except KeyboardInterrupt:
        return None


# ===============================================================================
def InputAddressAmount():
    print("\nPlease enter the amount of addresses to generate:")

    try:
        return input("   Address amount: ")
    except KeyboardInterrupt:
        return None


# ===============================================================================
def InputTargetAddress():
    print("\nPlease enter a target address with checksum:")

    try:
        return input("   Address: ")
    except KeyboardInterrupt:
        return None
