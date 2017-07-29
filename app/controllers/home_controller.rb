class HomeController < ApplicationController
  def index
    @data = { message: 'Hola Mundo Cruel!' }
  end
end
