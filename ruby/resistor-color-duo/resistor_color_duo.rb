=begin
Write your code for the 'Resistor Color Duo' exercise in this file. Make the tests in
`resistor_color_duo_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/resistor-color-duo` directory.
=end

class ResistorColorDuo
  def self.value(vals)
    lut = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue',
           'violet', 'grey', 'white']

    ret = 0
    vals[..1].each do |v|
      ret = ret * 10 + lut.index(v)
    end
    ret
  end
end
