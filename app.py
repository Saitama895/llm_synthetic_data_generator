from src.generator import generate_synthetic_data
from src.validator import seo_validate
from src.exporter import save_csv, save_json

# Generate synthetic SEO dataset
raw = generate_synthetic_data("AI Model Architectures", 20)

# Validate the generated data
clean = seo_validate(raw)
print(clean)

# Export the cleaned data
save_json(clean, "data/samples/seo_dataset.json")
save_csv(clean, "data/samples/seo_dataset.csv")

print(f"Saved {len(clean)} SEO samples")