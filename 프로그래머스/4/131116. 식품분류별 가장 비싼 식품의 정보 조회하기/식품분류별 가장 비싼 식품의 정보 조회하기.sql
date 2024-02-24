-- PRICE와 PRODUCT_NAME가 일치하지 않는 문제를 해결하려면 어떻게 해야 할까?
-- WHERE 문에서 두 항목을 묶어보자
SELECT CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
-- 2. 매핑된 조건에 맞는 CATEGORY, PRICE를 FOOD_PRODUCT에서 찾게 되므로, 이것에 이어지는 PRODUCT_NAME도 저절로 나온다
WHERE (CATEGORY, PRICE) IN (
    -- 1. 카테고리별 '카테고리:최대가격'이 매핑된 상태로 추출된다.
    SELECT CATEGORY, MAX(PRICE) 
    FROM FOOD_PRODUCT
    WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
    GROUP BY CATEGORY 
)
ORDER BY 2 DESC