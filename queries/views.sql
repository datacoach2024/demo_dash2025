set search_path to demo_dash;

create or replace view v_products as
select
	p.product_key
	, p.subcategory_key
	, p.product_name
	, p.standard_cost
	, coalesce(p.color, 'not_specified') as color
	, p.safety_stock_level
	, p.list_price
	, coalesce(p.product_size, 'not_specified') as product_size
	, p.product_weight
	, p.days_to_manufacture
	, coalesce(p.product_line, 'not_specified') as product_line
	, p.dealer_price
	, coalesce(p.product_class, 'not_specified') as product_class
	, p.model_name
	, p.start_date
	, p.end_date
	, p.product_status
	, ps.subcategory_name 
	, pc.category_name 
from products p
	left join product_subcategory ps 
		on p.subcategory_key = ps.subcategory_key
	left join product_category pc 
		on ps.category_key = pc.category_key 
where
	standard_cost is not null;

create or replace view v_sales as
select
	s.product_key      
	, s.order_date   
	, s.order_datekey
	, s.customer_key 
	, t.region 
	, t.country 
	, t.geo_group 
	, s.sales_order_number
	, s.sales_order_line_number
	, s.order_quantity
	, s.unit_price
	, s.total_product_cost
	, s.sales_amount
	, s.tax_amount
	, s.freight
	, s.sales_amount - s.tax_amount - s.freight as margin
from demo_dash.sales s
	left join demo_dash.territory t 
		on s.territory_key = t.territory_key 