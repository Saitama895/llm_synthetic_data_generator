from src.generator import generate_synthetic_data
from src.validator import seo_validate
from src.exporter import save_csv, save_json
import gradio as gr

def generate_seo_dataset(topic, num_samples):
    raw_data = generate_synthetic_data(topic, int(num_samples))
    clean_data = seo_validate(raw_data)
    return clean_data


with gr.Blocks(title="SEO Synthetic Dataset Generator") as demo:
    gr.Markdown("## 🔍 SEO Synthetic Dataset Generator (LLM-based)")
    gr.Markdown(
        "Generate high-quality instruction-input-output datasets "
        "optimized for SEO and LLM fine-tuning."
    )

    topic = gr.Textbox(
        label="SEO Topic / Keyword",
        placeholder="e.g. Transformer Encoder, CNN, LLM Fine-tuning"
    )

    samples = gr.Slider(
        minimum=5,
        maximum=100,
        step=5,
        value=20,
        label="Number of Samples"
    )

    generate_btn = gr.Button("Generate Dataset 🚀")

    output = gr.JSON(label="Generated Dataset")

    generate_btn.click(
        fn=generate_seo_dataset,
        inputs=[topic, samples],
        outputs=output
    )

demo.launch()




# # Export the cleaned data
# save_json(clean, "data/samples/seo_dataset.json")
# save_csv(clean, "data/samples/seo_dataset.csv")

# print(f"Saved {len(clean)} SEO samples")