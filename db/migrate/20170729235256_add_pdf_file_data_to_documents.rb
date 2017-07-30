class AddPdfFileDataToDocuments < ActiveRecord::Migration[5.1]
  def change
    add_column :documents, :pdf_file_data, :text
  end
end
