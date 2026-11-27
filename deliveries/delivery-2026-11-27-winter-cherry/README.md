# Approved Winter Cherry Blossom staging

The owner approved the Winter Cherry Blossom appearance in the complete Winter review array. This delivery adds that approved override to the existing Cherry Blossom draft, alongside its already approved base sprite.

## Changes

- Add `sprites/winter/cherry_blossom.png`, byte-identical to approved review card 12.
- Preserve the Cherry Blossom catalog entry, base PNG and previous draft work.
- Bring the draft forward onto the approved core Winter delivery, retaining the current purchase windows and all eleven core Winter overrides.
- Advance the Winter pack revision from 2 to 3 once for this additional seasonal sprite. The default Cherry Blossom sprite revision stays 1 because its base PNG is unchanged.
- Regenerate pack coverage. Autumn and Thanksgiving Cherry Blossom appearances remain gaps and fall back to the base sprite.

## Release decisions still pending

Cherry Blossom remains `enabled: false`, starts locked and retains the existing required 3-token placeholder. Its unlock, final store/placement price, availability and purchase window remain undecided. Winter remains disabled, with its current 10-token price and no newly chosen calendar window. Art approval alone does not enable either the tree or the pack.

## Source and validation

- Preserved PR #5 head: `aabcedcdb6999a6ad90fa6728300f55a465e63f6`.
- Base PNG SHA-256: `b8ce4826da20c8564a906d8160d7cfd736ad9fd422bab5e024f5a1a487745954`.
- Winter PNG SHA-256: `052b8124ae417c0697ef36a66a79c41fbe86cd1fb3ceeec57508c5927fee3a8e`.
- Both sprites use the 32×48 tree canvas, hard alpha and at most 16 opaque colors.
- Run the repository catalog validator, sprite checks and pack coverage check before publishing this draft update.

The historical core Winter delivery records revision 1 to 2. This later Cherry Blossom delivery records the separate revision 2 to 3 increment; neither rewrites the earlier delivery.
