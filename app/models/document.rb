class Document < ApplicationRecord
  default_scope { order(id: :desc) }

  include PdfFileUploader::Attachment.new(:pdf_file)

  belongs_to :user, optional: true

  validates :name, presence: true
  validates :category, inclusion: { in: ['pdf', 'url'] }
  # validates :file, presence: true, if: 'category =="pdf"'
  # validates :url,  presence: true, if: 'category == "url"'

end
