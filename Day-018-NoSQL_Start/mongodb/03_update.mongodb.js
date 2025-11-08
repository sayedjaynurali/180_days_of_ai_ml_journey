use("ecommerce")

// db.products.updateOne({"name":"Wireless Mouse"},{$set:{price:499}})

// db.products.find({"name":"Wireless Mouse"})

// db.products.updateMany(
//   { category: "changed category"},
//   {
//     $inc: { stock: 11 },
//     $set: { category: "Electronics" }
//   }
// )

db.products.updateOne(
    {
        "name": "Wireless Mouse",
    },
    {
        $push: {"tags":"new"}
    }
)