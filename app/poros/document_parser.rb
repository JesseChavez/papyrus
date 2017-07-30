class DocumentParser
  attr_reader :info
  attr_reader :page_count

  attr_reader :summary
  attr_reader :title

  def initialize(document)

      doc  = document.pdf_file.download
      @reader = PDF::Reader.new(doc.path)

      @title = @reader.info
      @page_count = @reader.page_count
      @content = []
      @reader.pages.each do |page|
        # puts "T---> #{page.text.squish}"
        # puts "T---> #{page.text.split("\n")}"
        # puts "T---> #{page.text.gsub(/\s+/, "\n")}"
        page.text.split("\n").each do |raw_line|
          line = raw_line.squish
          @content.push(line) unless line.blank?
        end
      end

      doc.delete
  end


  def process
    text = @content.join("\n\n")
    title = 'This is the title'

    context = ZMQ::Context.new

    requester = context.socket(ZMQ::REQ)
    requester.connect("tcp://127.0.0.1:5555")

    data = { title: title, text: text }

    requester.send_string data.to_json

    reply = ''

    requester.recv_string(reply)

    result = JSON.parse(reply)

    @summary =  result['text']
    @title = result['title']
  end
end
