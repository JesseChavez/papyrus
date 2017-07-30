class DocumentsController < ApplicationController
  def index
    @documents = Document.all

    render json: @documents.to_json, status: :ok
  end

  def show
    @document = Document.find(params[:id])

    render json: @document.to_json, status: :ok
  end

  def create
    @document = Document.new(document_params)
    @document.user_id = 1

    if @document.save
      doc = DocumentParser.new(@document)
      doc.process
      puts "-----: #{doc.summary}"
      puts "-----: #{doc.title}"
      render json: @document.to_json, status: :ok
    else
      render json: @document.errors, status: :unprocessable_entity
    end
  end

  def update
    @document = Document.find(params[:id])

    if @document.update(document_params)
      render json: @document.to_json, status: :ok
    else
      render json: @document.errors, status: :unprocessable_entity
    end
  end

  def destroy
  end

  private

  def document_params
    params.require(:document).permit(
      :name,
      :category,
      :pdf_file,
      :url,
      :remarks
    )
  end
end
