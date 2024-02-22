SELECT FIRST_HALF.FLAVOR 
FROM FIRST_HALF, ICECREAM_INFO
WHERE FIRST_HALF.TOTAL_ORDER > 3000 AND FIRST_HALF.FLAVOR = ICECREAM_INFO.FLAVOR AND ICECREAM_INFO.INGREDIENT_TYPE ='fruit_based' 
ORDER BY FIRST_HALF.TOTAL_ORDER DESC