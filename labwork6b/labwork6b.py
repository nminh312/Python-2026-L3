import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("scores.csv")

#scatter plot of student scores
for course in ["math", "python", "database"]:
    plt.scatter(df[course], df["student_id"], label=course)
plt.legend()
plt.grid(True)
plt.savefig("scattered.png")

#histograms in 3 subplots
df[["math", "python", "database"]].hist(bins=5, figsize=(10, 6))
plt.tight_layout()
plt.savefig("histro.png")

#single box plot for 3 courses
df[["math", "python", "database"]].plot(kind="box")
plt.savefig("box.png")