

SELECT 
  A.AUTHOR_ID, 
  B.AUTHOR_NAME, 
  A.CATEGORY,
  SUM(C.SALES * A.PRICE) AS TOTAL_SALES
FROM 
  BOOK A
JOIN 
  AUTHOR B ON A.AUTHOR_ID = B.AUTHOR_ID
JOIN 
  BOOK_SALES C ON C.BOOK_ID = A.BOOK_ID
WHERE 
  C.SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY 
  A.AUTHOR_ID, 
  A.CATEGORY
ORDER BY 
  A.AUTHOR_ID ASC, 
  A.CATEGORY DESC