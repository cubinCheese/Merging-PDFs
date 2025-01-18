import PyPDF2

def merge_pdfs(input_files, output_file):
    try:
        pdf_merger = PyPDF2.PdfMerger()

        # Add PDFs in the order they appear in the list
        for file in input_files:
            try:
                pdf_merger.append(file)
            except Exception as e:
                print(f"Error merging file {file}: {e}")
                raise

        # Write the merged PDF to the output file
        with open(output_file, "wb") as output:
            pdf_merger.write(output)

        print(f"Successfully merged PDFs into: {output_file}")

    except Exception as e:
        print(f"Error writing output file {output_file}: {e}")
        raise
