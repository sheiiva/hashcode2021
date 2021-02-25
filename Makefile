###########################################
#                 HASH CODE               #
###########################################
#                                         #
# Corentin COUTRET-ROZET and Hugo LACHKAR #
#                                         #
###########################################


NAME 	=	hashcode

RM 		=	@rm -f
PRINT	=	@echo -e

SOURCES		=	sources/


$(NAME):
	@cp $(SOURCES)main.py $@
	@chmod +x $@
	$(PRINT) "\n------->\tBINARY CREATED\n"

all: $(NAME)

clean:
	$(PRINT) "\n------->\tREMOVE PYCACHE\n"
	$(RM) -r __pycache__
	$(RM) -r $(SOURCES)__pycache__
	$(RM) -r $(SOURCES)sort/__pycache__
	$(RM) -r $(TESTS)__pycache__
	$(RM) -r $(TESTS)deps/__pycache__

fclean: clean
	$(PRINT) "\n------->\tREMOVE BINARY\n"
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean tests_run re