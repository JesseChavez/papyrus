class PdfFileUploader < Shrine
  plugin :activerecord
  plugin :determine_mime_type
  plugin :logging, logger: Rails.logger
  plugin :validation_helpers

  Attacher.validate do
    validate_max_size 10.megabytes, message: 'is too large (max is 10 MB)'
    # validate_mime_type_inclusion ['image/jpg', 'image/jpeg', 'image/png', 'image/gif']
    validate_mime_type_inclusion ['application/pdf']
  end
end
