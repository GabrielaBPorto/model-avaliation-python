import json
import os


size_key = "size"
threshold_range_key = "threshold_range"
values_key = "values"


def load_final_results(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
def calculate_metrics(tp, fp, fn):
    precision = tp / (tp + fp) if tp + fp != 0 else 0
    recall = tp / (tp + fn) if tp + fn != 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if precision + recall != 0 else 0
    return precision, recall, f1_score

def find_best_results(metrics):
    best_result = {"f1_score": 0}
    for size, data in metrics.items():
        for threshold, precision, recall, f1_score, tp, fp, fn in zip(
                data["thresholds"], data["precision"], data["recall"], 
                data["f1_score"], data["tp"], data["fp"], data["fn"]):

            if f1_score > best_result["f1_score"]:
                best_result = {
                    "size": size,
                    "threshold": threshold,
                    "precision": precision,
                    "recall": recall,
                    "f1_score": f1_score,
                    "tp": tp,
                    "fp": fp,
                    "fn": fn
                }
    return best_result

def print_best_results(best_result):
    print("Best Results:")
    print(f"Size: {best_result['size']}")
    print(f"Threshold: {best_result['threshold']}")
    print(f"Precision: {best_result['precision']}")
    print(f"Recall: {best_result['recall']}")
    print(f"F1-Score: {best_result['f1_score']}")
    print(f"True Positives (TP): {best_result['tp']}")
    print(f"False Positives (FP): {best_result['fp']}")
    print(f"False Negatives (FN): {best_result['fn']}")

def process_data(data):
    metrics = {}
    for size, info in data.items():
        metrics[size] = {
            "thresholds": [],
            "precision": [],
            "recall": [],
            "f1_score": [],
            "tp": [],
            "fp": [],
            "fn": []
        }
        for threshold, details in info["values"].items():
            tp, fp, fn = details["tp"], details["fp"], details["fn"]
            precision, recall, f1_score = calculate_metrics(tp, fp, fn)

            metrics[size]["thresholds"].append(threshold)
            metrics[size]["precision"].append(precision)
            metrics[size]["recall"].append(recall)
            metrics[size]["f1_score"].append(f1_score)
            metrics[size]["tp"].append(tp)
            metrics[size]["fp"].append(fp)
            metrics[size]["fn"].append(fn)

    return metrics

def print_metrics(metrics):
    for size, values in metrics.items():
        print(f"Size: {size}")
        for threshold, precision, recall, f1_score in zip(values["thresholds"], values["precision"], values["recall"], values["f1_score"]):
            print(f"  Threshold: {threshold:.2f}\n  Precision: {precision:.2f}\n  Recall: {recall:.2f}\n  F1-Score: {f1_score:.2f}\n")

def main():
    results_path = os.path.join(os.getcwd(), "temp", "resultados_finais.txt")
    
    if not os.path.exists(results_path):
        print("Arquivo de resultados finais não encontrado!")
        return
    
    final_results = load_final_results(results_path)
    metrics = process_data(final_results)
    best_result = find_best_results(metrics)
    print_best_results(best_result)


if __name__ == "__main__":
    main()
