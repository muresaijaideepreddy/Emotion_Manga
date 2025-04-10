import matplotlib.pyplot as plt

def plot_emotions(start_emotion, middle_emotion, end_emotion, output_path):
    steps = [0, 1, 2]
    labels = [start_emotion, middle_emotion, end_emotion]

    plt.plot(steps, [1, 2, 3], marker="o")
    plt.xticks(steps, labels)
    plt.title("Emotion Progression Across Manga Panels")
    plt.savefig(output_path)
