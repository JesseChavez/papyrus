class CreateDocuments < ActiveRecord::Migration[5.1]
  def change
    create_table :documents do |t|
      t.references :user, foreign_key: true
      t.string :category
      t.string :name
      t.text :remarks
      t.string :file_name
      t.string :url
      t.string :title
      t.text :meta_data
      t.text :summary
      t.text :content

      t.timestamps
    end
  end
end
