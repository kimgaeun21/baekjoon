-- 코드를 작성해주세요
select t.item_id, ni.item_name, ni.rarity
from item_info i
join 
item_tree t
on i.item_id = t.parent_item_id 
join 
item_info ni
on t.item_id = ni.item_id
where i.rarity = "RARE"
order by t.item_id desc