# Python for Javascript developers

Some ideas for notes I have about methods between languages

Want to have the returned element from an array based on matching object ids?

```
Javascript
const new_user = { id: "1234" }
const result = users_array.reduce((usr) => if(usr.id === new_user.id) user)[0];

Python
new_user = { id: "1234" }
result = [usr for usr in users_array if usr.id == new_user.id][0]
```
