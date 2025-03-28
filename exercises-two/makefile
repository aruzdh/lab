CC = gcc
CFLAGS = -I. -Iinclude -Itest/unity -Wall -Wextra 
UNITY_SRC = test/unity/unity.c
BUILD_DIR = build

TESTS = test_roman_to_int test_int_to_roman test_longest_common_prefix test_missing_and_repeated_value
TEST_EXES = $(addprefix $(BUILD_DIR)/, $(TESTS))

all: $(TEST_EXES)

$(BUILD_DIR)/test_roman_to_int: test/test_roman_to_int.c src/roman_to_int.c $(UNITY_SRC) | $(BUILD_DIR)
	$(CC) $(CFLAGS) -o $@ $^

$(BUILD_DIR)/test_int_to_roman: test/test_int_to_roman.c src/int_to_roman.c $(UNITY_SRC) | $(BUILD_DIR)
	$(CC) $(CFLAGS) -o $@ $^

$(BUILD_DIR)/test_longest_common_prefix: test/test_longest_common_prefix.c src/longest_common_prefix.c $(UNITY_SRC) | $(BUILD_DIR)
	$(CC) $(CFLAGS) -o $@ $^

$(BUILD_DIR)/test_missing_and_repeated_value: test/test_missing_and_repeated_value.c src/missing_and_repeated_value.c $(UNITY_SRC) | $(BUILD_DIR)
	$(CC) $(CFLAGS) -o $@ $^

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

run: all
	@for test in $(TESTS); do \
		./$(BUILD_DIR)/$$test || { echo "$$test has failed."; exit 1; }; \
	done
	@echo "Everything is well."

run_roman_to_int: $(BUILD_DIR)/test_roman_to_int
	./$(BUILD_DIR)/test_roman_to_int

run_int_to_roman: $(BUILD_DIR)/test_int_to_roman
	./$(BUILD_DIR)/test_int_to_roman

run_longest_common_prefix: $(BUILD_DIR)/test_longest_common_prefix
	./$(BUILD_DIR)/test_longest_common_prefix

run_missing_and_repeated_value: $(BUILD_DIR)/test_missing_and_repeated_value
	./$(BUILD_DIR)/test_missing_and_repeated_value

clean:
	rm -rf $(BUILD_DIR)

.PHONY: all run run_roman_to_int run_int_to_roman run_longest_common_prefix run_missing_and_repeated_value clean
