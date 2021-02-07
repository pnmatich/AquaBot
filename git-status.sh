curl \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/pnmatich/AquaBot/commits/7c5f16e729ad3aa8b47f453e55c04edfc6742bd8/status


https://api.github.com/pnmatich/AquaBot/commit/7c5f16e729ad3aa8b47f453e55c04edfc6742bd8

  curl \
    -X POST \
    -H "Accept: application/vnd.github.v3+json" \
    https://api.github.com/repos/pnmatich/AquaBot/statuses/7c5f16e729ad3aa8b47f453e55c04edfc6742bd8 \
    -d '{"state":"state"}' \
    -H "User-Agent: pmatich" \
    -H "Authorization: 94b399f40c662a3e22bbe2c223b4f3858db3a904"

    User-Agent: 'YOUR_USERNAME'
Authorization: 'token YOUR_TOKEN'
94b399f40c662a3e22bbe2c223b4f3858db3a904
