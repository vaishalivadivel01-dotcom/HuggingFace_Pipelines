import csv

# Read original text
with open("dataset/input_text.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    input_row = next(reader)

original_text = input_row["text"]


# Read summary
with open("dataset/summarized_text.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    summary_rows = list(reader)

summary = summary_rows[0]["Summary"]


# Read translation
with open("dataset/translated_text.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    translation_row = next(reader)

french = translation_row["French_Translation"]
spanish = translation_row["Spanish_Translation"]


# Read sentiment
with open("dataset/sentiment_results.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    sentiment_rows = list(reader)

sentiment = sentiment_rows[0]["Sentiment"]
score = sentiment_rows[0]["Score"]


# Read QA results
with open("dataset/qa_results.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    qa_rows = list(reader)

answers = ""

for row in qa_rows:
    answers += (
        "Q" + row["Question_No"]
        + ": " + row["Question"]
        + " | Answer: " + row["Answer"]
        + "\n"
    )


# Create comparison CSV
with open(
    "dataset/pipeline_comparison.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Original_Text",
        "Summary",
        "French_Translation",
        "Spanish_Translation",
        "Sentiment",
        "Sentiment_Score",
        "Question_Answers"
    ])

    writer.writerow([
        original_text,
        summary,
        french,
        spanish,
        sentiment,
        score,
        answers
    ])


print("=" * 60)
print("PIPELINE COMPARISON")
print("=" * 60)

print("\nComparison file created successfully!")

print("\nFile:")
print("dataset/pipeline_comparison.csv")

print("\nColumns:")
print("Original Text")
print("Summary")
print("French Translation")
print("Spanish Translation")
print("Sentiment")
print("Sentiment Score")
print("Question Answers")

print("\n" + "=" * 60)