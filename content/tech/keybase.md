Title: Keybase
Tags: identity
Summary: Identity Landing for Kenneth Bingham <w@qrk.us>

Here is a boring little post just to assert some crypto identities on an authenticated
platform which happens to be [@KeybaseIO](https://www.keybase.io).

This could enable me to trust your email signature when I only know you through Twitter,
and things like that.

The Keybase filesystem has a lot of promise. It is a global namespace with public and
private trees. The private tree allows any two parties have a truly confidential exchange
of data just by reading and writing in the special folders on their computer. You can look
over here for [more info about it](https://keybase.io/docs/kbfs).

This web page is housed in the kbfs at `/keybase/public/kourier`. The content is signed
during upload and so is verifiable by running the Keybase app on your computer, though it
is not obvious in your web browser.

If you install Keybase you'll be able to passively track changes in the web of identity
with commands like `keybase follow kourier`.

- You can send me secrets with Pretty Good Privacy by downloading my [pubkey](/blob/kourier-pgp-0xB69403FA957C5E46.asc) or importing it with GnuPG

        #!shell
        gpg --recv-keys "5489 E13F 8105 64DF 47FB  9841 B694 03FA 957C 5E46"

- You can grant privileges to my [Secure Shell (SSH)](/blob/kourier-ssh-id_rsa.pub) identity

        #!shell
        curl -s https://kourier.keybase.pub/kourier-ssh-id_rsa.pub >> .ssh/authorized_keys

[fork me](https://github.com/qrkourier/keybase-landing)