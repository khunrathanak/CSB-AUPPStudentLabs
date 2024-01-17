# Libraries you may need
import pandas as pd

# Classes and Functions to implement
class SchoolAssessmentSystem:
    def __init__(self):
        self.data = pd.DataFrame()

    def process_file(self, file_path, file_format):
        try:
            if file_format == 'csv':
                self.data = pd.read_csv(file_path)
            elif file_format == 'excel':
                self.data = pd.read_excel(file_path)
            elif file_format == 'text':
                with open(file_path, 'r') as file:
                    content = file.read()
                    print("Content read from file:")
                    print(content)
        except Exception as e:
            print(f"Error format, please change format of your file: {e}")
    def transfer_data(self,file_path,merge_path):
        try:
            # Read data from the input CSV files
            dataframes = [pd.read_csv(file_path) for file_path in file_path]

            # Concatenate the dataframes vertically (along rows)
            merged_df = pd.concat(dataframes, ignore_index=True)

            # Save the merged dataframe to the output CSV file
            merged_df.to_csv(merge_path, index=False)

            print("Merge successful. Merged data saved to", merge_path)
        except Exception as e:
            print("Error:", e)
         

    def fetch_web_data(self, url):
        try:
            return pd.read_csv(url)
        except (FileNotFoundError, pd.errors.EmptyDataError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            

    def analyze_content(self, data):
        try:
            # Assuming the relevant columns for scores are 'Math_Score', 'English_Score', etc.
            data['Total_Score'] = data[['INF 652', 'CSC 241', 'ITM 101', 'ITM 371', 'COSC 201']].sum(axis=1)
            
            # Calculate Total Average for each student
            data['Total_Average'] = data['Total_Score'] / 5  # Assuming 5 subjects
            
            # Identify the student with the highest and lowest Total Average
            top_student = data.loc[data['Total_Average'].idxmax()]
            lowest_student = data.loc[data['Total_Average'].idxmin()]
            
            # Calculate Semester-wise averages
            semester_averages = data.groupby('Semester')['Total_Average'].mean()

            # Identify the semester with the highest average
            best_semester = semester_averages.idxmax()

            return top_student, lowest_student, semester_averages, best_semester
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
    def generate_summary(self, result):
        if result:
            top_student, lowest_student,semester_averages, best_semester = result
            summary = f"Top Student:\n{top_student}\n\n" \
                      f"Lowest Student:\n{lowest_student}\n\n" \
                      f"Semester-wise Averages:\n{semester_averages}\n\n" \
                      f"Best Semester: {best_semester}"
            return summary
        else:
            return "Error occurred during analysis."

file_path = "data/all_semester.csv"  
data = pd.read_csv(file_path)

school_system = SchoolAssessmentSystem()
result = school_system.analyze_content(data)

summary = school_system.generate_summary(result)
print(summary)

