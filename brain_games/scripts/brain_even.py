#!/usr/bin/env python


from brain_games.game_engine.engine import engine
from brain_games.games.is_even import is_even_question, is_even_brief


def main():
    return engine(is_even_question, is_even_brief)


if __name__ == '__main__':
    main()
