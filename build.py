import os

# List of files in the order you want them combined
FILES = [
    "Libraries/MiscLibrary.pine",
    "Libraries/ChartDrawingLibrary.pine",
    "Libraries/MultiTimeFrameLibrary.pine",
    "Libraries/TradeManagerLibrary.pine",
    "Libraries/BooleanExpressionLibrary.pine",
    "Libraries/KeyLevelLibrary.pine",
    "Libraries/EntryStrategyLibrary.pine",
    "Strategies/FinalStrategy.pine"
]

OUTPUT_FILE = "final_output.pine"

def combine_files(file_list, output_path):
    with open(output_path, "w", encoding="utf-8") as outfile:
        for file_path in file_list:
            if not os.path.exists(file_path):
                print(f"⚠️ Warning: {file_path} does not exist, skipping.")
                continue

            with open(file_path, "r", encoding="utf-8") as infile:
                outfile.write(f"// === {file_path} ===\n")
                outfile.write(infile.read())
                outfile.write("\n\n")

    print(f"✅ Successfully generated: {output_path}")

if __name__ == "__main__":
    combine_files(FILES, OUTPUT_FILE)