# @param {Integer[]} nums
# @return {Integer[]}
def majority_element(nums)
    dict = Hash.new(0)
    nums.each do |i|
      dict[i] += 1
    end

    res = []
    compare = nums.length / 3
    dict.each do |key, value|
      res << key if value > compare
    end

    res
  end