# `Makefile` in options

This `Makefile` installs sets of `options` files to `${POUDRIERE_DIR}`,
`/usr/local/etc/poudriere.d` by default.

## Targets

### `install`

Install options files under `${OPTIONS_DIR}` to `${POUDRIERE_DIR}`. Run after
`poudriere ports -u`.

`poudriere(8)` does not provide a hook called when a ports tree is updated.
You need to either run `make(1)` manually after `poudriere ports -u`, or patch
`poudriere(8)`. See [my fork](https://github.com/trombik/poudriere/tree/ports_hooks).

## Updating `options` files

An example to update `options` for `ports-mgmt/poudriere-devel` in `devel`
branch:

```
cd ${PORTSDIR}
cd ports-mgmt/poudriere-devel
make config-recursive PORT_DBDIR=${PORTSDIR}/.config/options/devel-options
```

## Add a new set of `options`

Create a option directory. Add the directory name to `${OPTIONS_DIR}`. Copy
`options` files under the directory.

See "Custom build options" in `poudriere(8)`.
