"""A dependency-free gradient descent exercise, with reproducible toy data."""

import argparse
import json
import math
import random
from pathlib import Path


def make_data(seed):
    rng = random.Random(seed)
    points = []
    for _ in range(160):
        x = rng.uniform(-2.0, 2.0)
        points.append((x, 3.0 * x + 2.0 + rng.gauss(0.0, 0.2)))
    rng.shuffle(points)
    return points[:120], points[120:]


def mse(points, w, b):
    return sum((w * x + b - y) ** 2 for x, y in points) / len(points)


def train(lr, steps, seed):
    training, validation = make_data(seed)
    w = b = 0.0
    history = []
    status = "completed"
    for step in range(steps + 1):
        training_loss = mse(training, w, b)
        validation_loss = mse(validation, w, b)
        if not all(math.isfinite(v) for v in (w, b, training_loss, validation_loss)):
            status = "stopped_non_finite"
            break
        history.append({"step": step, "train_mse": training_loss,
                        "validation_mse": validation_loss, "w": w, "b": b})
        if max(training_loss, validation_loss) > 1e12:
            status = "stopped_large_loss"
            break
        if step == steps:
            break
        dw = 2.0 * sum((w * x + b - y) * x for x, y in training) / len(training)
        db = 2.0 * sum(w * x + b - y for x, y in training) / len(training)
        w -= lr * dw
        b -= lr * db
    return {"seed": seed, "learning_rate": lr, "requested_steps": steps,
            "train_size": len(training), "validation_size": len(validation),
            "data_rule": "y = 3*x + 2 + Gaussian(0, 0.2), x uniform in [-2, 2]",
            "status": status, "history": history}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lr", type=float, default=0.1)
    parser.add_argument("--steps", type=int, default=200)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if not math.isfinite(args.lr) or args.lr <= 0 or args.steps < 0:
        parser.error("learning rate must be finite and positive; steps must be nonnegative")
    result = train(args.lr, args.steps, args.seed)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "history"}, indent=2))
    print("initial:", result["history"][0])
    print("final:", result["history"][-1])


if __name__ == "__main__":
    main()
