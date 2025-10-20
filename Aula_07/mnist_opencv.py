import cv2
import numpy as np
import tensorflow as tf

MODEL_PATH = "mnist_model.h5"
WINDOW = "Webcam + MNIST Inference"

def prepare(img_gray, invert=False):
    # Resize to 28x28, normalize to [0,1], add channel and batch dims
    small = cv2.resize(img_gray, (28, 28), interpolation=cv2.INTER_AREA)
    if invert:
        small = 255 - small
    x = small.astype(np.float32) / 255.0
    x = x[None, ..., None]  # (1, 28, 28, 1)
    return small, x

def predict(model, x):
    y = model.predict(x, verbose=0)
    # Handle logits or probabilities, shape (1, 10) expected for MNIST
    y = tf.convert_to_tensor(y, dtype=tf.float32)
    probs = tf.nn.softmax(y, axis=-1).numpy()[0]
    cls = int(np.argmax(probs))
    conf = float(np.max(probs))
    return cls, conf, probs

def main():
    model = tf.keras.models.load_model(MODEL_PATH)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Cannot open webcam")

    invert = False
    font = cv2.FONT_HERSHEY_SIMPLEX

    while True:
        ok, frame = cap.read()
        if not ok:
            break
        display = frame.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        small28, x = prepare(gray, invert=invert)
        cls, conf, _ = predict(model, x)

        text = f"Pred: {cls}  ({conf*100:.1f}%)  [{'INV' if invert else 'NORM'}]"
        cv2.putText(display, text, (12, 34), font, 1.0, (0, 255, 0), 2, cv2.LINE_AA)

        small_vis = cv2.resize(small28, (112, 112), interpolation=cv2.INTER_NEAREST)
        small_vis_bgr = cv2.cvtColor(small_vis, cv2.COLOR_GRAY2BGR)
        
        h, w = display.shape[:2]
        margin = 10
        y_offset = h - 112 - margin
        x_offset = w - 112 - margin
        display[y_offset:y_offset+112, x_offset:x_offset+112] = small_vis_bgr

        cv2.imshow(WINDOW, display)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        if key == ord('i'):
            invert = not invert

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
