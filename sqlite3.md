
prepare statment on sqlite3 .

怕再度踩雷，記錄一下用法

```js
var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('ncnu.db');

db.serialize(function() {

  var stmt = db.prepare(`SELECT * FROM ncnu_info where faculty like ? and
                              department like ? and
                              division like ? and
                              course_credit like ? and
                              location like ? and
                              teacher like ? and
                              classtime like ? ;`);

  var data = ['%','%','%','%','%','%','%']
  stmt.each(data, function(err, row) {
      console.log(row);
  }, function(err, count) {
      stmt.finalize();
  });

});
```
