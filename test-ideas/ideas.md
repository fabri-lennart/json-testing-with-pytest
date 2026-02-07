# Core Data Transformation Test Cases (Pipeline-Focused)

Based on the CRM JSON structure, these are the **most relevant and realistic data transformation tests** for a data pipeline.

## 📥 Extraction & Normalization

- [✔️] Extract and flatten customer full name (`first_name + last_name`)
- [✔️] Extract and validate customer email format
- [ ] Flatten nested structures (`personal_info`, `address`, `company`, `engagement`)
- [ ] Normalize state names (e.g. "CDMX" → "Ciudad de México")
- [ ] Convert all date fields to ISO 8601 timestamps

## 🔄 Transformations & Enrichment

- [ ] Calculate customer age from `date_of_birth` and validate against provided `age`
- [ ] Derive `days_since_last_purchase` from `last_purchase_date`
- [ ] Create an `is_active_customer` flag based on status and recent purchases
- [ ] Assign LTV segment (`low`, `mid`, `high`) based on `lifetime_value`
- [ ] Assign company size category (`SMB`, `Mid-Market`, `Enterprise`) from `company.size`

## 📊 Aggregations & Metrics

- [ ] Calculate total revenue grouped by industry
- [ ] Calculate average lifetime_value per loyalty tier
- [ ] Count customers by country and state
- [ ] Identify top customers (top 10%) by lifetime_value

## 🧪 Data Quality & Consistency

- [ ] Validate that `tier` matches expected `loyalty_points` ranges
- [ ] Ensure `last_purchase_date` is not greater than current date
- [ ] Ensure inactive customers do not have recent purchase activity
- [ ] Validate uniqueness of customer `id`
---
