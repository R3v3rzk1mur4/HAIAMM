# PGP Encryption in HAIAMM

## Overview

HAIAMM uses PGP (Pretty Good Privacy) encryption to protect assessment data during export and import. All exported assessments are **encrypted and signed** to ensure confidentiality and authenticity.

## Why Encryption?

Assessment data contains sensitive security information:
- **Security gaps and vulnerabilities** identified during assessment
- **Implementation details** in notes and evidence fields
- **Organization names** and assessor identities
- **Maturity scores** revealing security posture

PGP encryption ensures:
- ✅ **Confidentiality**: Only the intended recipient can decrypt the file
- ✅ **Authenticity**: Digital signatures prove who created the export
- ✅ **Integrity**: Signatures detect any tampering with the file
- ✅ **Non-repudiation**: Signers cannot deny creating the export

---

## Prerequisites

### Install GPG/GnuPG

PGP encryption requires GPG to be installed on your system.

**macOS:**
```bash
brew install gnupg
```

**Ubuntu/Debian Linux:**
```bash
sudo apt install gnupg
```

**Fedora/RHEL:**
```bash
sudo dnf install gnupg
```

**Windows:**
Download Gpg4win from: https://gpg4win.org/download.html

**Verify Installation:**
```bash
gpg --version
```

You should see output starting with "gpg (GnuPG)".

### Generate Your PGP Key Pair

If you don't have a PGP key yet, generate one:

```bash
gpg --full-gen-key
```

Follow the prompts:
1. **Key type**: Select RSA (default)
2. **Key size**: 4096 bits (recommended)
3. **Expiration**: 2 years (recommended)
4. **Name**: Your full name
5. **Email**: Your email address
6. **Comment**: Optional (e.g., "HAIAMM signing key")
7. **Passphrase**: Choose a strong passphrase

**IMPORTANT:** Store your passphrase securely. You'll need it to sign exports and decrypt imports.

---

## Exporting Assessments

### Step-by-Step Export Process

1. **Open HAIAMM and load your assessment**
   - Select the assessment from the list
   - Click "Load Assessment" or double-click

2. **Start the export**
   - Click **File > Export Assessment** (or press Ctrl+E)
   - The Export Dialog will open

3. **Select export format**
   - **JSON (Complete assessment data)**: Full assessment with all metadata
   - **CSV (Responses only)**: Spreadsheet-compatible format

4. **Choose destination file**
   - Click "Browse..."
   - Select where to save the encrypted file
   - Files will have `.asc` extension (ASCII armored PGP)

5. **Select recipient's public key**
   - Click "Select Recipient Key"
   - Choose the recipient's public key from your keyring
   - The file will be encrypted so only they can decrypt it

6. **Select your signing key**
   - Click "Select Signing Key"
   - Choose your private key
   - This proves you created the export

7. **Enter your passphrase**
   - Type the passphrase for your private key
   - This is needed to create the digital signature

8. **Export**
   - Click "Export"
   - HAIAMM will encrypt and sign the file
   - You'll see a success message when complete

### Export File Format

Exported files use PGP ASCII armor format (`.asc`):

```
-----BEGIN PGP MESSAGE-----

hQIMA... [encrypted data] ...
-----END PGP MESSAGE-----
```

Inside the encrypted container is JSON data:
```json
{
  "format_version": "1.0",
  "export_metadata": {
    "exported_at": "2025-12-09T18:00:00Z",
    "application": "HAIAMM",
    "encryption_info": {
      "recipient_keyid": "ABCD1234",
      "signer_keyid": "EFGH5678"
    }
  },
  "assessment_data": {
    "name": "Q4 2025 Assessment",
    "organization": "Acme Corp",
    "responses": { ... }
  }
}
```

---

## Importing Assessments

### Step-by-Step Import Process

1. **Obtain the encrypted file**
   - Receive the `.asc` file from the sender
   - Save it to your computer

2. **Start the import**
   - Click **File > Import Assessment** (or press Ctrl+I)
   - The Import Dialog will open

3. **Select the encrypted file**
   - Click "Browse..."
   - Select the `.asc` file

4. **Enter your passphrase**
   - Type the passphrase for YOUR private key
   - This is needed to decrypt the file

5. **Decrypt and preview**
   - Click "Decrypt & Preview"
   - HAIAMM will decrypt and verify the signature

6. **Review signature verification**
   - **Valid signature (green)**: File is authentic and unmodified
     ```
     ✓ Signature Verified
     Signed by: Alice <alice@example.com>
     Trust Level: Full
     ```
   - **Invalid signature (red)**: Warning - file may be tampered with
     ```
     ⚠ Signature Verification Failed
     The signature could not be verified
     ```

7. **Review assessment details**
   - Check the assessment name, organization, and response count
   - Verify this is the correct file

8. **Import**
   - Click "Import"
   - The assessment will be saved to your database
   - A new assessment ID will be assigned (original ID is not preserved)

### Signature Verification

HAIAMM automatically verifies signatures when importing. This ensures:
- The file was created by the person who claims to have signed it
- The file has not been modified since signing
- The signer's key is in your GPG keyring

**If signature verification fails:**
- You can still import, but you'll see a warning
- This may indicate:
  - The signer's public key is not in your keyring
  - The file has been tampered with
  - The key is untrusted

**To trust a key:**
```bash
gpg --edit-key alice@example.com
trust
# Select trust level (usually '5' for ultimate)
quit
```

---

## Managing PGP Keys

### Listing Your Keys

**List public keys:**
```bash
gpg --list-keys
```

**List private keys:**
```bash
gpg --list-secret-keys
```

### Importing Someone's Public Key

**From a file:**
```bash
gpg --import alice-public-key.asc
```

**From a key server:**
```bash
gpg --recv-keys KEYID
```

### Exporting Your Public Key

To share with others so they can encrypt files for you:

```bash
gpg --armor --export your@email.com > my-public-key.asc
```

Send `my-public-key.asc` to anyone who needs to encrypt files for you.

### Backing Up Your Private Key

**CRITICAL:** Back up your private key securely!

```bash
gpg --armor --export-secret-keys your@email.com > my-private-key.asc
```

Store this file in a secure location (encrypted USB drive, password manager, etc.).

---

## Security Best Practices

### Passphrase Security

- ✅ Use a strong, unique passphrase (20+ characters)
- ✅ Store passphrase in a password manager
- ✅ Never share your passphrase
- ❌ Don't use the same passphrase as other accounts
- ❌ Don't write it on paper unless stored securely

### Key Management

- ✅ Generate separate keys for different purposes
- ✅ Set expiration dates (2 years recommended)
- ✅ Back up your private key securely
- ✅ Revoke compromised keys immediately
- ❌ Don't share your private key with anyone

### Export Security

- ✅ Always verify you selected the correct recipient key
- ✅ Use secure channels to share exported files (encrypted email, secure file transfer)
- ✅ Delete unencrypted files immediately
- ❌ Don't email unencrypted assessment files
- ❌ Don't store encrypted files in unprotected locations

### Import Security

- ✅ Always verify signatures before importing
- ✅ Only import from trusted sources
- ✅ Check the signer's identity matches expectations
- ❌ Don't import files with failed signature verification without investigation
- ❌ Don't trust keys without verifying ownership

---

## Troubleshooting

### "GPG Not Found" Error

**Problem:** HAIAMM can't find GPG on your system.

**Solution:**
1. Install GPG (see Prerequisites above)
2. Restart HAIAMM
3. Verify GPG is in your PATH: `which gpg` (macOS/Linux) or `where gpg` (Windows)

### "No Keys Found" Error

**Problem:** Your GPG keyring is empty.

**Solution:**
- Generate a key pair (see Prerequisites)
- Import existing keys

### "Invalid Passphrase" Error

**Problem:** Wrong passphrase entered.

**Solution:**
- Retype carefully (passphrases are case-sensitive)
- Verify you're using the correct key
- Reset passphrase if forgotten (requires access to secret key)

### "Signature Verification Failed" Error

**Problem:** Signature is invalid or untrusted.

**Possible causes:**
1. **Signer's public key not in keyring**: Import their public key
2. **Key is untrusted**: Trust the key manually (`gpg --edit-key`)
3. **File has been modified**: Contact the sender for a new copy
4. **Wrong key used**: Verify the signer's identity

**Solution:**
- Check signer's fingerprint with them out-of-band (phone call, in person)
- Import and trust their public key
- Request a new export if file is corrupted

### "Decryption Failed" Error

**Problem:** Can't decrypt the file.

**Possible causes:**
1. **Wrong passphrase**: Retype carefully
2. **File encrypted for different key**: Confirm with sender
3. **Corrupted file**: Request a new export

---

## Command-Line Reference

Useful GPG commands for key management:

```bash
# Generate new key pair
gpg --full-gen-key

# List all keys
gpg --list-keys
gpg --list-secret-keys

# Import a public key
gpg --import pubkey.asc

# Export your public key
gpg --armor --export your@email.com > pubkey.asc

# Export your private key (KEEP SECURE!)
gpg --armor --export-secret-keys your@email.com > privkey.asc

# Delete a public key
gpg --delete-keys keyid

# Delete a private key
gpg --delete-secret-keys keyid

# Edit key (change trust, expiration, etc.)
gpg --edit-key your@email.com

# Verify signature on a file
gpg --verify file.asc

# Decrypt a file manually
gpg --decrypt file.asc > output.json

# Encrypt a file manually
gpg --armor --recipient alice@example.com --sign --encrypt file.txt
```

---

## Audit Trail

HAIAMM logs all export and import operations for security audit purposes.

**What's logged:**
- Timestamp of operation
- Assessment ID
- Operation type (export/import)
- Recipient key ID (for exports)
- Signer key ID
- Signature validity (for imports)
- File path

**Accessing logs:**
The audit log is stored in the SQLite database (`export_audit_log` table).

**Query audit log:**
```sql
SELECT * FROM export_audit_log
WHERE assessment_id = <your_assessment_id>
ORDER BY timestamp DESC;
```

This provides a complete history of when and how assessments were exported/imported.

---

## FAQ

**Q: Can I export without encryption?**
A: No. All exports are encrypted and signed for security. This is a mandatory security requirement.

**Q: What if I lose my private key?**
A: You cannot decrypt files encrypted for that key. This is why backups are critical. Store your private key backup securely.

**Q: Can I use the same key for multiple computers?**
A: Yes, export your private key and import it on other machines. Be careful to keep it secure during transfer.

**Q: How do I share an assessment with someone?**
A:
1. Get their public key
2. Import it: `gpg --import their-pubkey.asc`
3. Export assessment, selecting their key as recipient
4. Send the encrypted `.asc` file to them

**Q: What if the recipient can't decrypt my export?**
A: Common causes:
- You selected the wrong recipient key
- They don't have the private key corresponding to the public key you used
- The file was corrupted during transfer

**Q: Are my passphrases stored by HAIAMM?**
A: No. HAIAMM never stores passphrases. They are only used temporarily for encryption/decryption and immediately cleared from memory.

**Q: Can I change my passphrase?**
A: Yes:
```bash
gpg --edit-key your@email.com
passwd
# Enter new passphrase
save
```

**Q: What encryption algorithms does HAIAMM use?**
A: HAIAMM uses whatever GPG's defaults are (typically RSA 4096-bit keys with AES-256 encryption). This is configured when you generate your keys.

---

## Support

For issues or questions about PGP encryption in HAIAMM:

1. Check this documentation
2. Review GPG documentation: https://gnupg.org/documentation/
3. File an issue: [Your GitHub repo]
4. Email support: [Your support email]

---

## Additional Resources

- **GnuPG Documentation**: https://gnupg.org/documentation/
- **GPG Quick Start**: https://gnupg.org/gph/en/manual.html
- **PGP Best Practices**: https://riseup.net/en/security/message-security/openpgp/best-practices
- **Key Servers**:
  - https://keys.openpgp.org/
  - https://keyserver.ubuntu.com/
