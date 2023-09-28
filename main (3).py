def linearSearchProduct(productList,targetProduct):
  indices=[]
  for index,product in enumerate(productList):
    if product==targetProduct:
      indices.append(index)
  return indices
#example usage
products=["shoes","boots","loafer","shoes","sandals","shoes"]
target1="shoes"
target2="apples"
result=linearSearchProduct(products,target1)
print(result)
