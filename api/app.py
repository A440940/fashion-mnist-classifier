import io
import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from .model_wrapper import ModelWrapper


model_wrapper = ModelWrapper()
app = FastAPI(title="Fashion MNIST classifier")


@app.get("/view-image")
def view_image(image_url: str):
    try:
        img = model_wrapper.load_image_from_url(image_url)

        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)

        return StreamingResponse(buf, media_type="image/png")
    except Exception as e:
        return {"error": str(e)}


@app.post("/classify-image")
def classify_image(image_url: str):
    try:
        predicted_class = model_wrapper.predict_from_url(image_url)
        return {"predicted_class": predicted_class}
    except Exception as e:
        return {"Error while tryning to predict image classe": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
