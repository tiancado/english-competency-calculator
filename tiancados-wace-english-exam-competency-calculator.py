import tkinter as tk
from tkinter import messagebox
import numpy as np

# Global variables for course data
# 2023, 2022, 2021, ..., 2018, 2017, 2016
years_data = {
    'eMSA_mean': [59.07, 58.54, 58.55, 57.79, 57.85, 58.84, 59.84, 59.84],  # English data
    'eMSA_std': [9.49, 9.77, 9.73, 9.88, 9.72, 9.97, 10.00, 10.43],
    'eREM_mean': [58.38, 57.75, 57.85, 57.05, 57.04, 58.15, 59.30, 59.10],
    'eREM_std': [11.19, 11.57, 11.11, 11.36, 11.11, 11.44, 11.26, 12.07],
    'eCS_mean': [58.75, 58.16, 58.22, 57.42, 57.46, 58.53, 59.60, 59.50],
    'eCS_std': [9.53, 9.89, 9.66, 9.80, 9.64, 9.95, 9.89, 10.42],
    'lMSA_mean': [66.79, 65.89, 64.48, 65.92, 67.76, 71.78, 67.81, 67.38],  # Literature data
    'lMSA_std': [8.87, 8.92, 9.41, 9.5, 9.19, 9.73, 9.34, 8.82],
    'lREM_mean': [66.11, 65.22, 63.88, 65.35, 67.15, 71.24, 67.27, 66.80],
    'lREM_std': [10.09, 10.27, 10.25, 10.56, 10.65, 10.10, 10.72, 9.73],
    'lCS_mean': [66.47, 65.56, 64.22, 65.65, 67.52, 71.58, 67.59, 67.18],
    'lCS_std': [8.69, 8.94, 9.18, 9.27, 9.18, 8.71, 9.30, 8.54],
    'acfMSA_mean': 65.2325, 'acfMSA_std': 17.25875,  # Accounting and Finance data
    'acfREM_mean': 64.44625, 'acfREM_std': 19.08875,
    'acfCS_mean': 59.345, 'acfCS_std': 17.795,
    'blyMSA_mean': 59.4675, 'blyMSA_std': 12.1,  # Biology data
    'blyREM_mean': 58.89, 'blyREM_std': 13.0225,
    'blyCS_mean': 59.1775, 'blyCS_std': 12.26,
    'cheMSA_mean': 59.86625, 'cheMSA_std': 16.90125,  # Chemistry data
    'cheREM_mean': 59.20875, 'cheREM_std': 18.05625,
    'cheCS_mean': 59.54375, 'cheCS_std': 17.20375,
    'cscMSA_mean': 60.09, 'cscMSA_std': 15.63,
    'cscREM_mean': 59.01125, 'cscREM_std': 17.2275,
    'cscCS_mean': 59.56375, 'cscCS_std': 15.99,
    'hbyMSA_mean': 60.19, 'hbyMSA_std': 13.2475,  # Human Biology data
    'hbyREM_mean': 59.59375, 'hbyREM_std': 14.1625,
    'hbyCS_mean': 59.88125, 'hbyCS_std': 13.39125,
    'maaMSA_mean': 60.90125, 'maaMSA_std': 15.08875,  # Mathematics Applications data
    'maaREM_mean': 60.05375, 'maaREM_std': 16.805,
    'maaCS_mean': 60.475, 'maaCS_std': 15.525,
    'mamMSA_mean': 64.5625, 'mamMSA_std': 17.7275,  # Mathematics Methods data
    'mamREM_mean': 63.9025, 'mamREM_std': 19.115,
    'mamCS_mean': 64.23125, 'mamCS_std': 18.11,
    'masMSA_mean': 63.01625, 'masMSA_std': 17.7425,  # Mathematics Specialists data
    'masREM_mean': 62.2575, 'masREM_std': 19.0275,
    'masCS_mean': 62.6475, 'masCS_std': 17.98,
    'phyMSA_mean': 59.0725, 'phyMSA_std': 17.78875,  # Physics data
    'phyREM_mean': 58.32, 'phyREM_std': 19.09875,
    'phyCS_mean': 58.72, 'phyCS_std': 18.14875,
    'palMSA_mean': 58.49, 'palMSA_std': 14.47,  # Politics and Law data
    'palREM_mean': 56.66625, 'palREM_std': 16.31125,
    'palCS_mean': 57.94, 'palCS_std': 15.01857143,
    'psyMSA_mean': 54.88375, 'psyMSA_std': 13.775,  # Psychology data
    'psyREM_mean': 53.90375, 'psyREM_std': 15.23875,
    'psyCS_mean': 54.415, 'psyCS_std': 14.04125,
    'relMSA_mean': 58.19125, 'relMSA_std': 10.4175,  # Religion and Life data
    'relREM_mean': 57.38125, 'relREM_std': 11.5125,
    'relCS_mean': 57.80875, 'relCS_std': 10.385
}


# Function to calculate the marks
def calculate(raw_school_mark, REM_mean, REM_std, MSA_mean, MSA_std, CS_mean, CS_std, cohort_mean, cohort_std_dev):
    raw_exam_mark = REM_mean + (raw_school_mark - cohort_mean) * (REM_std / cohort_std_dev)
    moderated_school_mark = MSA_mean + (raw_school_mark - cohort_mean) * (MSA_std / cohort_std_dev)
    combined_mark = (raw_exam_mark + moderated_school_mark) / 2
    scaled_combined_mark = 60 + (combined_mark - CS_mean) * (14 / CS_std)
    return raw_exam_mark, moderated_school_mark, combined_mark, scaled_combined_mark


# Main application class
class GradeCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("tiancado's WACE Marks Calculator")
        self.geometry("400x400")
        self.configure(bg="#f2f2f2")  # Background colour

        self.course_selection = tk.StringVar(self)
        self.course_selection.set("ATAR English")  # Default value

        self.create_widgets()

    def create_widgets(self):
        # Frame for the main content
        frame = tk.Frame(self, bg="#f2f2f2")
        frame.pack(pady=20)

        # Course selection dropdown
        tk.Label(frame, text="Select your course:", bg="#f2f2f2", font=("Arial", 12)).pack(pady=5)
        tk.OptionMenu(frame, self.course_selection, "ATAR Accounting and Finance",
                      "ATAR Biology", "ATAR Chemistry", "ATAR Computer Science", "ATAR English",
                      "ATAR Human Biology", "ATAR Literature", "ATAR Mathematics Applications",
                      "ATAR Mathematics Methods", "ATAR Mathematics Specialists", "ATAR Physics",
                      "ATAR Politics and Law", "ATAR Psychology", "ATAR Religion and Life").pack(pady=5)

        # Cohort mean
        tk.Label(frame, text="Enter your cohort/class's average/mean (in %):", bg="#f2f2f2", font=("Arial", 12)).pack(
            pady=5)
        self.cohort_mean_entry = tk.Entry(frame, font=("Arial", 12))
        self.cohort_mean_entry.pack(pady=5)

        # Cohort standard deviation
        tk.Label(frame, text="Enter your cohort/class's standard deviation:", bg="#f2f2f2", font=("Arial", 12)).pack(
            pady=5)
        self.cohort_std_entry = tk.Entry(frame, font=("Arial", 12))
        self.cohort_std_entry.pack(pady=5)

        # Raw school mark
        tk.Label(frame, text="Enter your raw school mark (in %):", bg="#f2f2f2", font=("Arial", 12)).pack(pady=5)
        self.raw_mark_entry = tk.Entry(frame, font=("Arial", 12))
        self.raw_mark_entry.pack(pady=5)

        # Calculate button
        calculate_button = tk.Button(frame, text="Calculate", command=self.calculate_marks, bg="#4CAF50", fg="white",
                                     font=("Arial", 12))
        calculate_button.pack(pady=20)

    def calculate_marks(self):
        try:
            cohort_mean = float(self.cohort_mean_entry.get())
            cohort_std_dev = float(self.cohort_std_entry.get())
            raw_school_mark = float(self.raw_mark_entry.get())

            # Select course data based on the user's choice
            # "ATAR Accounting and Finance", "ATAR Biology", "ATAR Chemistry", "ATAR Computer Science", "ATAR English",
            # "ATAR Human Biology", "ATAR Literature", "ATAR Mathematics Applications",
            # "ATAR Mathematics Methods", "ATAR Mathematics Specialists", "ATAR Physics",
            # "ATAR Politics and Law", "ATAR Psychology", "ATAR Religion and Life")
            course_selection = self.course_selection.get()
            if course_selection == "ATAR English":
                MSA_mean = np.mean(years_data['eMSA_mean'])
                MSA_std = np.mean(years_data['eMSA_std'])
                REM_mean = np.mean(years_data['eREM_mean'])
                REM_std = np.mean(years_data['eREM_std'])
                CS_mean = np.mean(years_data['eCS_mean'])
                CS_std = np.mean(years_data['eCS_std'])
            elif course_selection == "ATAR Literature":
                MSA_mean = np.mean(years_data['lMSA_mean'])
                MSA_std = np.mean(years_data['lMSA_std'])
                REM_mean = np.mean(years_data['lREM_mean'])
                REM_std = np.mean(years_data['lREM_std'])
                CS_mean = np.mean(years_data['lCS_mean'])
                CS_std = np.mean(years_data['lCS_std'])
            elif course_selection == "ATAR Biology":
                MSA_mean = years_data['blyMSA_mean']
                MSA_std = years_data['blyMSA_std']
                REM_mean = years_data['blyREM_mean']
                REM_std = years_data['blyREM_std']
                CS_mean = years_data['blyCS_mean']
                CS_std = years_data['blyCS_std']
            elif course_selection == "ATAR Accounting and Finance":
                MSA_mean = years_data['acfMSA_mean']
                MSA_std = years_data['acfMSA_std']
                REM_mean = years_data['acfREM_mean']
                REM_std = years_data['acfREM_std']
                CS_mean = years_data['acfCS_mean']
                CS_std = years_data['acfCS_std']
            elif course_selection == "ATAR Chemistry":
                MSA_mean = years_data['cheMSA_mean']
                MSA_std = years_data['cheMSA_std']
                REM_mean = years_data['cheREM_mean']
                REM_std = years_data['cheREM_std']
                CS_mean = years_data['cheCS_mean']
                CS_std = years_data['cheCS_std']
            elif course_selection == "ATAR Computer Science":
                MSA_mean = years_data['cscMSA_mean']
                MSA_std = years_data['cscMSA_std']
                REM_mean = years_data['cscREM_mean']
                REM_std = years_data['cscREM_std']
                CS_mean = years_data['cscCS_mean']
                CS_std = years_data['cheCS_std']
            elif course_selection == "ATAR Human Biology":
                MSA_mean = years_data['hbyMSA_mean']
                MSA_std = years_data['hbyMSA_std']
                REM_mean = years_data['hbyREM_mean']
                REM_std = years_data['hbyREM_std']
                CS_mean = years_data['cscCS_mean']
                CS_std = years_data['cscCS_std']
            elif course_selection == "ATAR Mathematics Applications":
                MSA_mean = years_data['maaMSA_mean']
                MSA_std = years_data['maaMSA_std']
                REM_mean = years_data['maaREM_mean']
                REM_std = years_data['maaREM_std']
                CS_mean = years_data['maaCS_mean']
                CS_std = years_data['maaCS_std']
            elif course_selection == "ATAR Mathematics Methods":
                MSA_mean = years_data['mamMSA_mean']
                MSA_std = years_data['mamMSA_std']
                REM_mean = years_data['mamREM_mean']
                REM_std = years_data['mamREM_std']
                CS_mean = years_data['mamCS_mean']
                CS_std = years_data['mamCS_std']
            elif course_selection == "ATAR Mathematics Specialists":
                MSA_mean = years_data['masMSA_mean']
                MSA_std = years_data['masMSA_std']
                REM_mean = years_data['masREM_mean']
                REM_std = years_data['masREM_std']
                CS_mean = years_data['masCS_mean']
                CS_std = years_data['masCS_std']
            elif course_selection == "ATAR Physics":
                MSA_mean = years_data['phyMSA_mean']
                MSA_std = years_data['phyMSA_std']
                REM_mean = years_data['phyREM_mean']
                REM_std = years_data['phyREM_std']
                CS_mean = years_data['phyCS_mean']
                CS_std = years_data['phyCS_std']
            elif course_selection == "ATAR Politics and Law":
                MSA_mean = years_data['palMSA_mean']
                MSA_std = years_data['palMSA_std']
                REM_mean = years_data['palREM_mean']
                REM_std = years_data['palREM_std']
                CS_mean = years_data['palCS_mean']
                CS_std = years_data['palCS_std']
            elif course_selection == "ATAR Psychology":
                MSA_mean = years_data['psyMSA_mean']
                MSA_std = years_data['psyMSA_std']
                REM_mean = years_data['psyREM_mean']
                REM_std = years_data['psyREM_std']
                CS_mean = years_data['psyCS_mean']
                CS_std = years_data['psyCS_std']
            elif course_selection == "ATAR Religion and Life":
                MSA_mean = years_data['relMSA_mean']
                MSA_std = years_data['relMSA_std']
                REM_mean = years_data['relREM_mean']
                REM_std = years_data['relREM_std']
                CS_mean = years_data['relCS_mean']
                CS_std = years_data['relCS_std']

            # Calculate marks
            raw_exam_mark, moderated_school_mark, combined_mark, scaled_combined_mark = calculate(
                raw_school_mark, REM_mean, REM_std, MSA_mean, MSA_std, CS_mean, CS_std, cohort_mean, cohort_std_dev)

            # Show result in message box
            messagebox.showinfo("Results", f"Extrapolated Raw Exam Mark: {round(raw_exam_mark, 2)}%\n"
                                           f"Moderated School Mark: {round(moderated_school_mark, 2)}%\n"
                                           f"Unscaled Combined Mark: {round(combined_mark, 2)}%\n"
                                           f"Scaled Combined Mark: {round(scaled_combined_mark, 2)}%")

        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numerical values.")


# Run the application
if __name__ == "__main__":
    app = GradeCalculatorApp()
    app.mainloop()
