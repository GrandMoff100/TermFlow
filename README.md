# ``termflow``
## Terminal Flowcharts

This project does not work and has been abandoned. However I will except PRs for new development from other people.

# Examples
```
 0 ─  1 ─  2 ─  3     5 ─ 6 ─ 7
                 \   /
                   4
                 /   \
0a ─ 1a ─ 2a ─ 3a     5a ─ 6a ─ 7a
```

```
  c ── f 
 /      \
a        g
 \      /
  b ── e
```

```
             store hash
               ^
               |                   
fail  <- sig check <- encrypt(password) + encryption algo
               ^                                 ^
               |                                 |      
Server -> new secret key -> encryption algo -> client
```
