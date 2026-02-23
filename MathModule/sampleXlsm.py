from openpyxl import Workbook
import zipfile
import os

# Create a macro-enabled workbook (.xlsm)
from openpyxl import Workbook
from openpyxl.writer.excel import save_workbook

# File path
file_path = "/mnt/data/sample_macro.xlsm"

# Sample data for Sheet1
data = [
    ["ID", "Name", "Status"],
    [1, "John", "Pass"],
    [2, "Alice", "Fail"],
    [3, "Bob", "Pass"],
    [4, "Charlie", "Fail"]
]

# Create a workbook and add data to Sheet1
wb = Workbook()
ws1 = wb.active
ws1.title = "Sheet1"

for row in data:
    ws1.append(row)

# Add second sheet (form-like)
ws2 = wb.create_sheet("Sheet2")
ws2["A1"] = "Enter Details Below:"
ws2["A2"] = "Name"
ws2["B2"] = ""
ws2["A3"] = "Status"
ws2["B3"] = ""

# Save workbook (temporarily as xlsx, we'll convert structure to xlsm manually)
temp_xlsx_path = "/mnt/data/temp_file.xlsx"
wb.save(temp_xlsx_path)

# Macro VBA code (in plaintext, will be injected into xlsm)
vba_code = """
Sub HighlightFails()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Sheet1")
    
    Dim lastRow As Long
    lastRow = ws.Cells(ws.Rows.Count, "C").End(xlUp).Row

    Dim i As Long
    For i = 2 To lastRow
        If ws.Cells(i, 3).Value = "Fail" Then
            ws.Rows(i).Interior.Color = RGB(255, 199, 206)
        End If
    Next i
End Sub
"""

# To make it a real .xlsm file, we need a binary vbaProject.bin (manually created or extracted from Excel)
# Since we can't generate binary vbaProject.bin from Python directly, we'll prepare the .xlsm structurally but it won't contain a live macro unless user injects vbaProject.bin

# Instead, inform user to inject the macro manually in Excel's VBA editor

# Rename the file extension to .xlsm for testing purposes
os.rename(temp_xlsx_path, file_path)

file_path
