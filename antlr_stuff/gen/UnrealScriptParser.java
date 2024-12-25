// Generated from ./UnrealScript.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class UnrealScriptParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, T__40=41, T__41=42, T__42=43, T__43=44, T__44=45, 
		T__45=46, T__46=47, T__47=48, T__48=49, T__49=50, T__50=51, T__51=52, 
		T__52=53, T__53=54, T__54=55, T__55=56, T__56=57, StringVal=58, NameVal=59, 
		IntVal=60, FloatVal=61, BoolVal=62, NoneVal=63, VectVal=64, ABSTRACT=65, 
		ARRAY=66, ASSERT=67, AUTO=68, BOOL=69, BYTE=70, CASE=71, CLASS=72, COERCE=73, 
		COLLAPSECATEGORIES=74, CONFIG=75, CONST=76, CONSTRUCTIVE=77, DEFAULT=78, 
		DEFAULTPROPERTIES=79, DELEGATE=80, DEPENDSON=81, DEPRECATED=82, DO=83, 
		DONTCOLLAPSECATEGORIES=84, DYNAMICRECOMPILE=85, EDFINDABLE=86, EDITCONST=87, 
		EDITINLINE=88, EDITINLINENEW=89, EDITINLINENOTIFY=90, EDITINLINEUSE=91, 
		ELSE=92, ENUM=93, EVENT=94, EXEC=95, EXPORT=96, EXPORTSTRUCTS=97, EXTENDS=98, 
		FINAL=99, FLOAT=100, FOR=101, FOREACH=102, FUNCTION=103, GLOBALCONFIG=104, 
		HIDECATEGORIES=105, IF=106, IGNORES=107, INPUT=108, INT=109, ITERATOR=110, 
		LATENT=111, LOCAL=112, LOCALIZED=113, NAME=114, NATIVE=115, NATIVEREPLICATION=116, 
		NEW=117, NOEXPORT=118, NONATIVEREPLICATION=119, NOTEDITINLINENEW=120, 
		NOTPLACEABLE=121, OPERATOR=122, OPTIONAL=123, OUT=124, PEROBJECTCONFIG=125, 
		PLACEABLE=126, POSTOPERATOR=127, PREOPERATOR=128, PRIVATE=129, PROTECTED=130, 
		RELIABLE=131, REPLICATION=132, RETURN=133, SAFEREPLACE=134, SELF=135, 
		SHOWCATEGORIES=136, SIMULATED=137, SINGULAR=138, SKIP_=139, STATE=140, 
		STATIC=141, STRING=142, STRUCT=143, SWITCH=144, TRANSIENT=145, TRAVEL=146, 
		UNRELIABLE=147, UNTIL=148, VAR=149, WHILE=150, WITHIN=151, IDENT=152, 
		WS=153, DIRECTIVE=154, COMMENT=155, LINE_COMMENT=156;
	public static final int
		RULE_program = 0, RULE_classdecl = 1, RULE_classparams = 2, RULE_constclassparams = 3, 
		RULE_identifier = 4, RULE_packageidentifier = 5, RULE_declarations = 6, 
		RULE_constdecl = 7, RULE_constvalue = 8, RULE_classval = 9, RULE_objectval = 10, 
		RULE_vardecl = 11, RULE_arrayindex = 12, RULE_varparams = 13, RULE_configgroup = 14, 
		RULE_vartype = 15, RULE_basictype = 16, RULE_varidentifier = 17, RULE_arraydecl = 18, 
		RULE_dynarraydecl = 19, RULE_classtype = 20, RULE_enumdecl = 21, RULE_enumoptions = 22, 
		RULE_structdecl = 23, RULE_structparams = 24, RULE_structbody = 25, RULE_replicationblock = 26, 
		RULE_replicationbody = 27, RULE_body = 28, RULE_statedecl = 29, RULE_statebody = 30, 
		RULE_stateignore = 31, RULE_statelabels = 32, RULE_stateparams = 33, RULE_functiondecl = 34, 
		RULE_normalfunc = 35, RULE_functiontype = 36, RULE_functionparams = 37, 
		RULE_constfuncparams = 38, RULE_operatorfunc = 39, RULE_operatortype = 40, 
		RULE_binaryoperator = 41, RULE_unaryoperator = 42, RULE_opidentifier = 43, 
		RULE_operatornames = 44, RULE_functionargs = 45, RULE_functionargtype = 46, 
		RULE_functionbody = 47, RULE_localdecl = 48, RULE_localtype = 49, RULE_codeblock = 50, 
		RULE_statement = 51, RULE_assertion = 52, RULE_ifstatement = 53, RULE_switchstatement = 54, 
		RULE_whileloop = 55, RULE_doloop = 56, RULE_foreachloop = 57, RULE_forloop = 58, 
		RULE_returnstatement = 59, RULE_caserule = 60, RULE_casecodeblock = 61, 
		RULE_defaultrule = 62, RULE_expression = 63, RULE_primary = 64, RULE_creator = 65, 
		RULE_parExpression = 66, RULE_expressionList = 67, RULE_defaultpropertiesblock = 68, 
		RULE_defprop = 69, RULE_defpropidentifier = 70, RULE_qualifiedidentifier = 71, 
		RULE_identifierlist = 72;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "classdecl", "classparams", "constclassparams", "identifier", 
			"packageidentifier", "declarations", "constdecl", "constvalue", "classval", 
			"objectval", "vardecl", "arrayindex", "varparams", "configgroup", "vartype", 
			"basictype", "varidentifier", "arraydecl", "dynarraydecl", "classtype", 
			"enumdecl", "enumoptions", "structdecl", "structparams", "structbody", 
			"replicationblock", "replicationbody", "body", "statedecl", "statebody", 
			"stateignore", "statelabels", "stateparams", "functiondecl", "normalfunc", 
			"functiontype", "functionparams", "constfuncparams", "operatorfunc", 
			"operatortype", "binaryoperator", "unaryoperator", "opidentifier", "operatornames", 
			"functionargs", "functionargtype", "functionbody", "localdecl", "localtype", 
			"codeblock", "statement", "assertion", "ifstatement", "switchstatement", 
			"whileloop", "doloop", "foreachloop", "forloop", "returnstatement", "caserule", 
			"casecodeblock", "defaultrule", "expression", "primary", "creator", "parExpression", 
			"expressionList", "defaultpropertiesblock", "defprop", "defpropidentifier", 
			"qualifiedidentifier", "identifierlist"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'('", "')'", "'.'", "'='", "','", "'['", "']'", "'<'", 
			"'>'", "'{'", "'}'", "':'", "'~'", "'!'", "'@'", "'#'", "'$'", "'%'", 
			"'^'", "'&'", "'*'", "'-'", "'+'", "'|'", "'\\'", "'/'", "'?'", "'`'", 
			"'<<'", "'>>'", "'!='", "'<='", "'>='", "'++'", "'--'", "'?-'", "'+='", 
			"'-='", "'*='", "'/='", "'&&'", "'||'", "'^^'", "'=='", "'**'", "'~='", 
			"'@='", "'>>>'", "'&='", "'|='", "'^='", "'>>='", "'>>>='", "'<<='", 
			"'%='", "'''"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, "StringVal", 
			"NameVal", "IntVal", "FloatVal", "BoolVal", "NoneVal", "VectVal", "ABSTRACT", 
			"ARRAY", "ASSERT", "AUTO", "BOOL", "BYTE", "CASE", "CLASS", "COERCE", 
			"COLLAPSECATEGORIES", "CONFIG", "CONST", "CONSTRUCTIVE", "DEFAULT", "DEFAULTPROPERTIES", 
			"DELEGATE", "DEPENDSON", "DEPRECATED", "DO", "DONTCOLLAPSECATEGORIES", 
			"DYNAMICRECOMPILE", "EDFINDABLE", "EDITCONST", "EDITINLINE", "EDITINLINENEW", 
			"EDITINLINENOTIFY", "EDITINLINEUSE", "ELSE", "ENUM", "EVENT", "EXEC", 
			"EXPORT", "EXPORTSTRUCTS", "EXTENDS", "FINAL", "FLOAT", "FOR", "FOREACH", 
			"FUNCTION", "GLOBALCONFIG", "HIDECATEGORIES", "IF", "IGNORES", "INPUT", 
			"INT", "ITERATOR", "LATENT", "LOCAL", "LOCALIZED", "NAME", "NATIVE", 
			"NATIVEREPLICATION", "NEW", "NOEXPORT", "NONATIVEREPLICATION", "NOTEDITINLINENEW", 
			"NOTPLACEABLE", "OPERATOR", "OPTIONAL", "OUT", "PEROBJECTCONFIG", "PLACEABLE", 
			"POSTOPERATOR", "PREOPERATOR", "PRIVATE", "PROTECTED", "RELIABLE", "REPLICATION", 
			"RETURN", "SAFEREPLACE", "SELF", "SHOWCATEGORIES", "SIMULATED", "SINGULAR", 
			"SKIP_", "STATE", "STATIC", "STRING", "STRUCT", "SWITCH", "TRANSIENT", 
			"TRAVEL", "UNRELIABLE", "UNTIL", "VAR", "WHILE", "WITHIN", "IDENT", "WS", 
			"DIRECTIVE", "COMMENT", "LINE_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "UnrealScript.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public UnrealScriptParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public ClassdeclContext classdecl() {
			return getRuleContext(ClassdeclContext.class,0);
		}
		public List<DeclarationsContext> declarations() {
			return getRuleContexts(DeclarationsContext.class);
		}
		public DeclarationsContext declarations(int i) {
			return getRuleContext(DeclarationsContext.class,i);
		}
		public List<ReplicationblockContext> replicationblock() {
			return getRuleContexts(ReplicationblockContext.class);
		}
		public ReplicationblockContext replicationblock(int i) {
			return getRuleContext(ReplicationblockContext.class,i);
		}
		public List<BodyContext> body() {
			return getRuleContexts(BodyContext.class);
		}
		public BodyContext body(int i) {
			return getRuleContext(BodyContext.class,i);
		}
		public DefaultpropertiesblockContext defaultpropertiesblock() {
			return getRuleContext(DefaultpropertiesblockContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			classdecl();
			setState(152);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 68)) & ~0x3f) == 0 && ((1L << (_la - 68)) & 8665079651430830337L) != 0) || ((((_la - 132)) & ~0x3f) == 0 && ((1L << (_la - 132)) & 133985L) != 0)) {
				{
				setState(150);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case CONST:
				case ENUM:
				case STRUCT:
				case VAR:
					{
					setState(147);
					declarations();
					}
					break;
				case REPLICATION:
					{
					setState(148);
					replicationblock();
					}
					break;
				case AUTO:
				case DELEGATE:
				case EVENT:
				case EXEC:
				case FINAL:
				case FUNCTION:
				case ITERATOR:
				case LATENT:
				case NATIVE:
				case OPERATOR:
				case POSTOPERATOR:
				case PREOPERATOR:
				case PRIVATE:
				case PROTECTED:
				case SIMULATED:
				case SINGULAR:
				case STATE:
				case STATIC:
					{
					setState(149);
					body();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(154);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(156);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DEFAULTPROPERTIES) {
				{
				setState(155);
				defaultpropertiesblock();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClassdeclContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(UnrealScriptParser.CLASS, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode EXTENDS() { return getToken(UnrealScriptParser.EXTENDS, 0); }
		public PackageidentifierContext packageidentifier() {
			return getRuleContext(PackageidentifierContext.class,0);
		}
		public List<ClassparamsContext> classparams() {
			return getRuleContexts(ClassparamsContext.class);
		}
		public ClassparamsContext classparams(int i) {
			return getRuleContext(ClassparamsContext.class,i);
		}
		public ClassdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classdecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterClassdecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitClassdecl(this);
		}
	}

	public final ClassdeclContext classdecl() throws RecognitionException {
		ClassdeclContext _localctx = new ClassdeclContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_classdecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			match(CLASS);
			setState(159);
			identifier();
			setState(162);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EXTENDS) {
				{
				setState(160);
				match(EXTENDS);
				setState(161);
				packageidentifier();
				}
			}

			setState(167);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & 3597251306187195905L) != 0) || ((((_la - 134)) & ~0x3f) == 0 && ((1L << (_la - 134)) & 133125L) != 0)) {
				{
				{
				setState(164);
				classparams();
				}
				}
				setState(169);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(170);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClassparamsContext extends ParserRuleContext {
		public ConstclassparamsContext constclassparams() {
			return getRuleContext(ConstclassparamsContext.class,0);
		}
		public TerminalNode WITHIN() { return getToken(UnrealScriptParser.WITHIN, 0); }
		public PackageidentifierContext packageidentifier() {
			return getRuleContext(PackageidentifierContext.class,0);
		}
		public TerminalNode DEPENDSON() { return getToken(UnrealScriptParser.DEPENDSON, 0); }
		public TerminalNode CONFIG() { return getToken(UnrealScriptParser.CONFIG, 0); }
		public TerminalNode HIDECATEGORIES() { return getToken(UnrealScriptParser.HIDECATEGORIES, 0); }
		public IdentifierlistContext identifierlist() {
			return getRuleContext(IdentifierlistContext.class,0);
		}
		public TerminalNode SHOWCATEGORIES() { return getToken(UnrealScriptParser.SHOWCATEGORIES, 0); }
		public ClassparamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classparams; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterClassparams(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitClassparams(this);
		}
	}

	public final ClassparamsContext classparams() throws RecognitionException {
		ClassparamsContext _localctx = new ClassparamsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_classparams);
		int _la;
		try {
			setState(197);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ABSTRACT:
			case COLLAPSECATEGORIES:
			case DONTCOLLAPSECATEGORIES:
			case DYNAMICRECOMPILE:
			case EDITINLINENEW:
			case EXPORTSTRUCTS:
			case NATIVE:
			case NATIVEREPLICATION:
			case NOEXPORT:
			case NONATIVEREPLICATION:
			case NOTEDITINLINENEW:
			case NOTPLACEABLE:
			case PEROBJECTCONFIG:
			case PLACEABLE:
			case SAFEREPLACE:
			case TRANSIENT:
				enterOuterAlt(_localctx, 1);
				{
				setState(172);
				constclassparams();
				}
				break;
			case WITHIN:
				enterOuterAlt(_localctx, 2);
				{
				setState(173);
				match(WITHIN);
				setState(174);
				packageidentifier();
				}
				break;
			case DEPENDSON:
				enterOuterAlt(_localctx, 3);
				{
				setState(175);
				match(DEPENDSON);
				setState(176);
				match(T__1);
				setState(177);
				packageidentifier();
				setState(178);
				match(T__2);
				}
				break;
			case CONFIG:
				enterOuterAlt(_localctx, 4);
				{
				setState(180);
				match(CONFIG);
				setState(185);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__1) {
					{
					setState(181);
					match(T__1);
					setState(182);
					packageidentifier();
					setState(183);
					match(T__2);
					}
				}

				}
				break;
			case HIDECATEGORIES:
				enterOuterAlt(_localctx, 5);
				{
				setState(187);
				match(HIDECATEGORIES);
				setState(188);
				match(T__1);
				setState(189);
				identifierlist();
				setState(190);
				match(T__2);
				}
				break;
			case SHOWCATEGORIES:
				enterOuterAlt(_localctx, 6);
				{
				setState(192);
				match(SHOWCATEGORIES);
				setState(193);
				match(T__1);
				setState(194);
				identifierlist();
				setState(195);
				match(T__2);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstclassparamsContext extends ParserRuleContext {
		public TerminalNode ABSTRACT() { return getToken(UnrealScriptParser.ABSTRACT, 0); }
		public TerminalNode NATIVE() { return getToken(UnrealScriptParser.NATIVE, 0); }
		public TerminalNode NATIVEREPLICATION() { return getToken(UnrealScriptParser.NATIVEREPLICATION, 0); }
		public TerminalNode NONATIVEREPLICATION() { return getToken(UnrealScriptParser.NONATIVEREPLICATION, 0); }
		public TerminalNode SAFEREPLACE() { return getToken(UnrealScriptParser.SAFEREPLACE, 0); }
		public TerminalNode PEROBJECTCONFIG() { return getToken(UnrealScriptParser.PEROBJECTCONFIG, 0); }
		public TerminalNode TRANSIENT() { return getToken(UnrealScriptParser.TRANSIENT, 0); }
		public TerminalNode NOEXPORT() { return getToken(UnrealScriptParser.NOEXPORT, 0); }
		public TerminalNode EXPORTSTRUCTS() { return getToken(UnrealScriptParser.EXPORTSTRUCTS, 0); }
		public TerminalNode COLLAPSECATEGORIES() { return getToken(UnrealScriptParser.COLLAPSECATEGORIES, 0); }
		public TerminalNode DONTCOLLAPSECATEGORIES() { return getToken(UnrealScriptParser.DONTCOLLAPSECATEGORIES, 0); }
		public TerminalNode PLACEABLE() { return getToken(UnrealScriptParser.PLACEABLE, 0); }
		public TerminalNode NOTPLACEABLE() { return getToken(UnrealScriptParser.NOTPLACEABLE, 0); }
		public TerminalNode EDITINLINENEW() { return getToken(UnrealScriptParser.EDITINLINENEW, 0); }
		public TerminalNode NOTEDITINLINENEW() { return getToken(UnrealScriptParser.NOTEDITINLINENEW, 0); }
		public TerminalNode DYNAMICRECOMPILE() { return getToken(UnrealScriptParser.DYNAMICRECOMPILE, 0); }
		public ConstclassparamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constclassparams; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterConstclassparams(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitConstclassparams(this);
		}
	}

	public final ConstclassparamsContext constclassparams() throws RecognitionException {
		ConstclassparamsContext _localctx = new ConstclassparamsContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_constclassparams);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(199);
			_la = _input.LA(1);
			if ( !(((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & 3597250206675501569L) != 0) || _la==SAFEREPLACE || _la==TRANSIENT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdentifierContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(UnrealScriptParser.IDENT, 0); }
		public TerminalNode ABSTRACT() { return getToken(UnrealScriptParser.ABSTRACT, 0); }
		public TerminalNode ARRAY() { return getToken(UnrealScriptParser.ARRAY, 0); }
		public TerminalNode ASSERT() { return getToken(UnrealScriptParser.ASSERT, 0); }
		public TerminalNode AUTO() { return getToken(UnrealScriptParser.AUTO, 0); }
		public TerminalNode BOOL() { return getToken(UnrealScriptParser.BOOL, 0); }
		public TerminalNode BYTE() { return getToken(UnrealScriptParser.BYTE, 0); }
		public TerminalNode CASE() { return getToken(UnrealScriptParser.CASE, 0); }
		public TerminalNode CLASS() { return getToken(UnrealScriptParser.CLASS, 0); }
		public TerminalNode COERCE() { return getToken(UnrealScriptParser.COERCE, 0); }
		public TerminalNode COLLAPSECATEGORIES() { return getToken(UnrealScriptParser.COLLAPSECATEGORIES, 0); }
		public TerminalNode CONFIG() { return getToken(UnrealScriptParser.CONFIG, 0); }
		public TerminalNode CONST() { return getToken(UnrealScriptParser.CONST, 0); }
		public TerminalNode CONSTRUCTIVE() { return getToken(UnrealScriptParser.CONSTRUCTIVE, 0); }
		public TerminalNode DEFAULT() { return getToken(UnrealScriptParser.DEFAULT, 0); }
		public TerminalNode DEFAULTPROPERTIES() { return getToken(UnrealScriptParser.DEFAULTPROPERTIES, 0); }
		public TerminalNode DELEGATE() { return getToken(UnrealScriptParser.DELEGATE, 0); }
		public TerminalNode DEPENDSON() { return getToken(UnrealScriptParser.DEPENDSON, 0); }
		public TerminalNode DEPRECATED() { return getToken(UnrealScriptParser.DEPRECATED, 0); }
		public TerminalNode DO() { return getToken(UnrealScriptParser.DO, 0); }
		public TerminalNode DONTCOLLAPSECATEGORIES() { return getToken(UnrealScriptParser.DONTCOLLAPSECATEGORIES, 0); }
		public TerminalNode DYNAMICRECOMPILE() { return getToken(UnrealScriptParser.DYNAMICRECOMPILE, 0); }
		public TerminalNode EDFINDABLE() { return getToken(UnrealScriptParser.EDFINDABLE, 0); }
		public TerminalNode EDITCONST() { return getToken(UnrealScriptParser.EDITCONST, 0); }
		public TerminalNode EDITINLINE() { return getToken(UnrealScriptParser.EDITINLINE, 0); }
		public TerminalNode EDITINLINENEW() { return getToken(UnrealScriptParser.EDITINLINENEW, 0); }
		public TerminalNode EDITINLINENOTIFY() { return getToken(UnrealScriptParser.EDITINLINENOTIFY, 0); }
		public TerminalNode EDITINLINEUSE() { return getToken(UnrealScriptParser.EDITINLINEUSE, 0); }
		public TerminalNode ELSE() { return getToken(UnrealScriptParser.ELSE, 0); }
		public TerminalNode ENUM() { return getToken(UnrealScriptParser.ENUM, 0); }
		public TerminalNode EVENT() { return getToken(UnrealScriptParser.EVENT, 0); }
		public TerminalNode EXEC() { return getToken(UnrealScriptParser.EXEC, 0); }
		public TerminalNode EXPORT() { return getToken(UnrealScriptParser.EXPORT, 0); }
		public TerminalNode EXPORTSTRUCTS() { return getToken(UnrealScriptParser.EXPORTSTRUCTS, 0); }
		public TerminalNode EXTENDS() { return getToken(UnrealScriptParser.EXTENDS, 0); }
		public TerminalNode FINAL() { return getToken(UnrealScriptParser.FINAL, 0); }
		public TerminalNode FLOAT() { return getToken(UnrealScriptParser.FLOAT, 0); }
		public TerminalNode FOR() { return getToken(UnrealScriptParser.FOR, 0); }
		public TerminalNode FOREACH() { return getToken(UnrealScriptParser.FOREACH, 0); }
		public TerminalNode FUNCTION() { return getToken(UnrealScriptParser.FUNCTION, 0); }
		public TerminalNode GLOBALCONFIG() { return getToken(UnrealScriptParser.GLOBALCONFIG, 0); }
		public TerminalNode HIDECATEGORIES() { return getToken(UnrealScriptParser.HIDECATEGORIES, 0); }
		public TerminalNode IF() { return getToken(UnrealScriptParser.IF, 0); }
		public TerminalNode IGNORES() { return getToken(UnrealScriptParser.IGNORES, 0); }
		public TerminalNode INPUT() { return getToken(UnrealScriptParser.INPUT, 0); }
		public TerminalNode INT() { return getToken(UnrealScriptParser.INT, 0); }
		public TerminalNode ITERATOR() { return getToken(UnrealScriptParser.ITERATOR, 0); }
		public TerminalNode LATENT() { return getToken(UnrealScriptParser.LATENT, 0); }
		public TerminalNode LOCAL() { return getToken(UnrealScriptParser.LOCAL, 0); }
		public TerminalNode LOCALIZED() { return getToken(UnrealScriptParser.LOCALIZED, 0); }
		public TerminalNode NAME() { return getToken(UnrealScriptParser.NAME, 0); }
		public TerminalNode NATIVE() { return getToken(UnrealScriptParser.NATIVE, 0); }
		public TerminalNode NATIVEREPLICATION() { return getToken(UnrealScriptParser.NATIVEREPLICATION, 0); }
		public TerminalNode NEW() { return getToken(UnrealScriptParser.NEW, 0); }
		public TerminalNode NOEXPORT() { return getToken(UnrealScriptParser.NOEXPORT, 0); }
		public TerminalNode NONATIVEREPLICATION() { return getToken(UnrealScriptParser.NONATIVEREPLICATION, 0); }
		public TerminalNode NOTEDITINLINENEW() { return getToken(UnrealScriptParser.NOTEDITINLINENEW, 0); }
		public TerminalNode NOTPLACEABLE() { return getToken(UnrealScriptParser.NOTPLACEABLE, 0); }
		public TerminalNode OPERATOR() { return getToken(UnrealScriptParser.OPERATOR, 0); }
		public TerminalNode OPTIONAL() { return getToken(UnrealScriptParser.OPTIONAL, 0); }
		public TerminalNode OUT() { return getToken(UnrealScriptParser.OUT, 0); }
		public TerminalNode PEROBJECTCONFIG() { return getToken(UnrealScriptParser.PEROBJECTCONFIG, 0); }
		public TerminalNode PLACEABLE() { return getToken(UnrealScriptParser.PLACEABLE, 0); }
		public TerminalNode POSTOPERATOR() { return getToken(UnrealScriptParser.POSTOPERATOR, 0); }
		public TerminalNode PREOPERATOR() { return getToken(UnrealScriptParser.PREOPERATOR, 0); }
		public TerminalNode PRIVATE() { return getToken(UnrealScriptParser.PRIVATE, 0); }
		public TerminalNode PROTECTED() { return getToken(UnrealScriptParser.PROTECTED, 0); }
		public TerminalNode RELIABLE() { return getToken(UnrealScriptParser.RELIABLE, 0); }
		public TerminalNode REPLICATION() { return getToken(UnrealScriptParser.REPLICATION, 0); }
		public TerminalNode RETURN() { return getToken(UnrealScriptParser.RETURN, 0); }
		public TerminalNode SAFEREPLACE() { return getToken(UnrealScriptParser.SAFEREPLACE, 0); }
		public TerminalNode SELF() { return getToken(UnrealScriptParser.SELF, 0); }
		public TerminalNode SHOWCATEGORIES() { return getToken(UnrealScriptParser.SHOWCATEGORIES, 0); }
		public TerminalNode SIMULATED() { return getToken(UnrealScriptParser.SIMULATED, 0); }
		public TerminalNode SINGULAR() { return getToken(UnrealScriptParser.SINGULAR, 0); }
		public TerminalNode SKIP_() { return getToken(UnrealScriptParser.SKIP_, 0); }
		public TerminalNode STATE() { return getToken(UnrealScriptParser.STATE, 0); }
		public TerminalNode STATIC() { return getToken(UnrealScriptParser.STATIC, 0); }
		public TerminalNode STRING() { return getToken(UnrealScriptParser.STRING, 0); }
		public TerminalNode STRUCT() { return getToken(UnrealScriptParser.STRUCT, 0); }
		public TerminalNode SWITCH() { return getToken(UnrealScriptParser.SWITCH, 0); }
		public TerminalNode TRANSIENT() { return getToken(UnrealScriptParser.TRANSIENT, 0); }
		public TerminalNode TRAVEL() { return getToken(UnrealScriptParser.TRAVEL, 0); }
		public TerminalNode UNRELIABLE() { return getToken(UnrealScriptParser.UNRELIABLE, 0); }
		public TerminalNode UNTIL() { return getToken(UnrealScriptParser.UNTIL, 0); }
		public TerminalNode VAR() { return getToken(UnrealScriptParser.VAR, 0); }
		public TerminalNode WHILE() { return getToken(UnrealScriptParser.WHILE, 0); }
		public TerminalNode WITHIN() { return getToken(UnrealScriptParser.WITHIN, 0); }
		public IdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterIdentifier(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitIdentifier(this);
		}
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_identifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			_la = _input.LA(1);
			if ( !(((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & -1L) != 0) || ((((_la - 129)) & ~0x3f) == 0 && ((1L << (_la - 129)) & 16777215L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PackageidentifierContext extends ParserRuleContext {
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public PackageidentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_packageidentifier; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterPackageidentifier(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitPackageidentifier(this);
		}
	}

	public final PackageidentifierContext packageidentifier() throws RecognitionException {
		PackageidentifierContext _localctx = new PackageidentifierContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_packageidentifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(206);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(203);
				identifier();
				setState(204);
				match(T__3);
				}
				break;
			}
			setState(208);
			identifier();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationsContext extends ParserRuleContext {
		public ConstdeclContext constdecl() {
			return getRuleContext(ConstdeclContext.class,0);
		}
		public VardeclContext vardecl() {
			return getRuleContext(VardeclContext.class,0);
		}
		public EnumdeclContext enumdecl() {
			return getRuleContext(EnumdeclContext.class,0);
		}
		public StructdeclContext structdecl() {
			return getRuleContext(StructdeclContext.class,0);
		}
		public DeclarationsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarations; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterDeclarations(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitDeclarations(this);
		}
	}

	public final DeclarationsContext declarations() throws RecognitionException {
		DeclarationsContext _localctx = new DeclarationsContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_declarations);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(214);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CONST:
				{
				setState(210);
				constdecl();
				}
				break;
			case VAR:
				{
				setState(211);
				vardecl();
				}
				break;
			case ENUM:
				{
				setState(212);
				enumdecl();
				}
				break;
			case STRUCT:
				{
				setState(213);
				structdecl();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(216);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstdeclContext extends ParserRuleContext {
		public TerminalNode CONST() { return getToken(UnrealScriptParser.CONST, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ConstdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constdecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterConstdecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitConstdecl(this);
		}
	}

	public final ConstdeclContext constdecl() throws RecognitionException {
		ConstdeclContext _localctx = new ConstdeclContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_constdecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(218);
			match(CONST);
			setState(219);
			identifier();
			setState(220);
			match(T__4);
			setState(221);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstvalueContext extends ParserRuleContext {
		public TerminalNode StringVal() { return getToken(UnrealScriptParser.StringVal, 0); }
		public TerminalNode NameVal() { return getToken(UnrealScriptParser.NameVal, 0); }
		public TerminalNode IntVal() { return getToken(UnrealScriptParser.IntVal, 0); }
		public TerminalNode FloatVal() { return getToken(UnrealScriptParser.FloatVal, 0); }
		public TerminalNode BoolVal() { return getToken(UnrealScriptParser.BoolVal, 0); }
		public TerminalNode NoneVal() { return getToken(UnrealScriptParser.NoneVal, 0); }
		public ClassvalContext classval() {
			return getRuleContext(ClassvalContext.class,0);
		}
		public ObjectvalContext objectval() {
			return getRuleContext(ObjectvalContext.class,0);
		}
		public TerminalNode VectVal() { return getToken(UnrealScriptParser.VectVal, 0); }
		public ConstvalueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constvalue; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterConstvalue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitConstvalue(this);
		}
	}

	public final ConstvalueContext constvalue() throws RecognitionException {
		ConstvalueContext _localctx = new ConstvalueContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_constvalue);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(223);
				match(StringVal);
				}
				break;
			case 2:
				{
				setState(224);
				match(NameVal);
				}
				break;
			case 3:
				{
				setState(225);
				match(IntVal);
				}
				break;
			case 4:
				{
				setState(226);
				match(FloatVal);
				}
				break;
			case 5:
				{
				setState(227);
				match(BoolVal);
				}
				break;
			case 6:
				{
				setState(228);
				match(NoneVal);
				}
				break;
			case 7:
				{
				setState(229);
				classval();
				}
				break;
			case 8:
				{
				setState(230);
				objectval();
				}
				break;
			case 9:
				{
				setState(231);
				match(VectVal);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClassvalContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(UnrealScriptParser.CLASS, 0); }
		public TerminalNode NameVal() { return getToken(UnrealScriptParser.NameVal, 0); }
		public ClassvalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classval; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterClassval(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitClassval(this);
		}
	}

	public final ClassvalContext classval() throws RecognitionException {
		ClassvalContext _localctx = new ClassvalContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_classval);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			match(CLASS);
			setState(235);
			match(NameVal);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ObjectvalContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode NameVal() { return getToken(UnrealScriptParser.NameVal, 0); }
		public ObjectvalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_objectval; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterObjectval(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitObjectval(this);
		}
	}

	public final ObjectvalContext objectval() throws RecognitionException {
		ObjectvalContext _localctx = new ObjectvalContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_objectval);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(237);
			identifier();
			setState(238);
			match(NameVal);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VardeclContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(UnrealScriptParser.VAR, 0); }
		public VartypeContext vartype() {
			return getRuleContext(VartypeContext.class,0);
		}
		public List<VaridentifierContext> varidentifier() {
			return getRuleContexts(VaridentifierContext.class);
		}
		public VaridentifierContext varidentifier(int i) {
			return getRuleContext(VaridentifierContext.class,i);
		}
		public ConfiggroupContext configgroup() {
			return getRuleContext(ConfiggroupContext.class,0);
		}
		public List<VarparamsContext> varparams() {
			return getRuleContexts(VarparamsContext.class);
		}
		public VarparamsContext varparams(int i) {
			return getRuleContext(VarparamsContext.class,i);
		}
		public List<ArrayindexContext> arrayindex() {
			return getRuleContexts(ArrayindexContext.class);
		}
		public ArrayindexContext arrayindex(int i) {
			return getRuleContext(ArrayindexContext.class,i);
		}
		public VardeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterVardecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitVardecl(this);
		}
	}

	public final VardeclContext vardecl() throws RecognitionException {
		VardeclContext _localctx = new VardeclContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_vardecl);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(240);
			match(VAR);
			setState(242);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(241);
				configgroup();
				}
			}

			setState(247);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(244);
					varparams();
					}
					} 
				}
				setState(249);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			}
			setState(250);
			vartype();
			setState(251);
			varidentifier();
			setState(253);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__6) {
				{
				setState(252);
				arrayindex();
				}
			}

			setState(262);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(255);
				match(T__5);
				setState(256);
				varidentifier();
				setState(258);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__6) {
					{
					setState(257);
					arrayindex();
					}
				}

				}
				}
				setState(264);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArrayindexContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ArrayindexContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayindex; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterArrayindex(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitArrayindex(this);
		}
	}

	public final ArrayindexContext arrayindex() throws RecognitionException {
		ArrayindexContext _localctx = new ArrayindexContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_arrayindex);
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(265);
			match(T__6);
			setState(266);
			expression(0);
			setState(267);
			match(T__7);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarparamsContext extends ParserRuleContext {
		public TerminalNode CONFIG() { return getToken(UnrealScriptParser.CONFIG, 0); }
		public TerminalNode CONST() { return getToken(UnrealScriptParser.CONST, 0); }
		public TerminalNode EDITCONST() { return getToken(UnrealScriptParser.EDITCONST, 0); }
		public TerminalNode EXPORT() { return getToken(UnrealScriptParser.EXPORT, 0); }
		public TerminalNode GLOBALCONFIG() { return getToken(UnrealScriptParser.GLOBALCONFIG, 0); }
		public TerminalNode INPUT() { return getToken(UnrealScriptParser.INPUT, 0); }
		public TerminalNode LOCALIZED() { return getToken(UnrealScriptParser.LOCALIZED, 0); }
		public TerminalNode NATIVE() { return getToken(UnrealScriptParser.NATIVE, 0); }
		public TerminalNode PRIVATE() { return getToken(UnrealScriptParser.PRIVATE, 0); }
		public TerminalNode PROTECTED() { return getToken(UnrealScriptParser.PROTECTED, 0); }
		public TerminalNode TRANSIENT() { return getToken(UnrealScriptParser.TRANSIENT, 0); }
		public TerminalNode TRAVEL() { return getToken(UnrealScriptParser.TRAVEL, 0); }
		public TerminalNode EDITINLINE() { return getToken(UnrealScriptParser.EDITINLINE, 0); }
		public TerminalNode DEPRECATED() { return getToken(UnrealScriptParser.DEPRECATED, 0); }
		public TerminalNode EDFINDABLE() { return getToken(UnrealScriptParser.EDFINDABLE, 0); }
		public TerminalNode EDITINLINEUSE() { return getToken(UnrealScriptParser.EDITINLINEUSE, 0); }
		public TerminalNode EDITINLINENOTIFY() { return getToken(UnrealScriptParser.EDITINLINENOTIFY, 0); }
		public VarparamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varparams; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterVarparams(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitVarparams(this);
		}
	}

	public final VarparamsContext varparams() throws RecognitionException {
		VarparamsContext _localctx = new VarparamsContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_varparams);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(269);
			_la = _input.LA(1);
			if ( !(((((_la - 75)) & ~0x3f) == 0 && ((1L << (_la - 75)) & 54044579046996099L) != 0) || _la==TRANSIENT || _la==TRAVEL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConfiggroupContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public ConfiggroupContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_configgroup; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterConfiggroup(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitConfiggroup(this);
		}
	}

	public final ConfiggroupContext configgroup() throws RecognitionException {
		ConfiggroupContext _localctx = new ConfiggroupContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_configgroup);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(271);
			match(T__1);
			setState(273);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & -1L) != 0) || ((((_la - 129)) & ~0x3f) == 0 && ((1L << (_la - 129)) & 16777215L) != 0)) {
				{
				setState(272);
				identifier();
				}
			}

			setState(275);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VartypeContext extends ParserRuleContext {
		public ArraydeclContext arraydecl() {
			return getRuleContext(ArraydeclContext.class,0);
		}
		public DynarraydeclContext dynarraydecl() {
			return getRuleContext(DynarraydeclContext.class,0);
		}
		public PackageidentifierContext packageidentifier() {
			return getRuleContext(PackageidentifierContext.class,0);
		}
		public EnumdeclContext enumdecl() {
			return getRuleContext(EnumdeclContext.class,0);
		}
		public StructdeclContext structdecl() {
			return getRuleContext(StructdeclContext.class,0);
		}
		public ClasstypeContext classtype() {
			return getRuleContext(ClasstypeContext.class,0);
		}
		public BasictypeContext basictype() {
			return getRuleContext(BasictypeContext.class,0);
		}
		public VartypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vartype; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterVartype(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitVartype(this);
		}
	}

	public final VartypeContext vartype() throws RecognitionException {
		VartypeContext _localctx = new VartypeContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_vartype);
		try {
			setState(284);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(277);
				arraydecl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(278);
				dynarraydecl();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(279);
				packageidentifier();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(280);
				enumdecl();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(281);
				structdecl();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(282);
				classtype();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(283);
				basictype();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BasictypeContext extends ParserRuleContext {
		public TerminalNode BYTE() { return getToken(UnrealScriptParser.BYTE, 0); }
		public TerminalNode INT() { return getToken(UnrealScriptParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(UnrealScriptParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(UnrealScriptParser.STRING, 0); }
		public TerminalNode BOOL() { return getToken(UnrealScriptParser.BOOL, 0); }
		public TerminalNode NAME() { return getToken(UnrealScriptParser.NAME, 0); }
		public BasictypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_basictype; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterBasictype(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitBasictype(this);
		}
	}

	public final BasictypeContext basictype() throws RecognitionException {
		BasictypeContext _localctx = new BasictypeContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_basictype);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(286);
			_la = _input.LA(1);
			if ( !(((((_la - 69)) & ~0x3f) == 0 && ((1L << (_la - 69)) & 36286031200259L) != 0) || _la==STRING) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VaridentifierContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public VaridentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varidentifier; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterVaridentifier(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitVaridentifier(this);
		}
	}

	public final VaridentifierContext varidentifier() throws RecognitionException {
		VaridentifierContext _localctx = new VaridentifierContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_varidentifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(288);
			identifier();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArraydeclContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ArraydeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arraydecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterArraydecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitArraydecl(this);
		}
	}

	public final ArraydeclContext arraydecl() throws RecognitionException {
		ArraydeclContext _localctx = new ArraydeclContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_arraydecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(290);
			identifier();
			setState(291);
			match(T__6);
			setState(293);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & -288230273047281660L) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & -1L) != 0) || ((((_la - 128)) & ~0x3f) == 0 && ((1L << (_la - 128)) & 33554431L) != 0)) {
				{
				setState(292);
				expression(0);
				}
			}

			setState(295);
			match(T__7);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DynarraydeclContext extends ParserRuleContext {
		public TerminalNode ARRAY() { return getToken(UnrealScriptParser.ARRAY, 0); }
		public PackageidentifierContext packageidentifier() {
			return getRuleContext(PackageidentifierContext.class,0);
		}
		public ClasstypeContext classtype() {
			return getRuleContext(ClasstypeContext.class,0);
		}
		public BasictypeContext basictype() {
			return getRuleContext(BasictypeContext.class,0);
		}
		public List<VarparamsContext> varparams() {
			return getRuleContexts(VarparamsContext.class);
		}
		public VarparamsContext varparams(int i) {
			return getRuleContext(VarparamsContext.class,i);
		}
		public DynarraydeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dynarraydecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterDynarraydecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitDynarraydecl(this);
		}
	}

	public final DynarraydeclContext dynarraydecl() throws RecognitionException {
		DynarraydeclContext _localctx = new DynarraydeclContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_dynarraydecl);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(297);
			match(ARRAY);
			setState(298);
			match(T__8);
			setState(302);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(299);
					varparams();
					}
					} 
				}
				setState(304);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			}
			setState(308);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				{
				setState(305);
				packageidentifier();
				}
				break;
			case 2:
				{
				setState(306);
				classtype();
				}
				break;
			case 3:
				{
				setState(307);
				basictype();
				}
				break;
			}
			setState(310);
			match(T__9);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClasstypeContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(UnrealScriptParser.CLASS, 0); }
		public PackageidentifierContext packageidentifier() {
			return getRuleContext(PackageidentifierContext.class,0);
		}
		public ClasstypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classtype; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterClasstype(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitClasstype(this);
		}
	}

	public final ClasstypeContext classtype() throws RecognitionException {
		ClasstypeContext _localctx = new ClasstypeContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_classtype);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(312);
			match(CLASS);
			setState(317);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				{
				setState(313);
				match(T__8);
				setState(314);
				packageidentifier();
				setState(315);
				match(T__9);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EnumdeclContext extends ParserRuleContext {
		public TerminalNode ENUM() { return getToken(UnrealScriptParser.ENUM, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public EnumoptionsContext enumoptions() {
			return getRuleContext(EnumoptionsContext.class,0);
		}
		public EnumdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_enumdecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterEnumdecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitEnumdecl(this);
		}
	}

	public final EnumdeclContext enumdecl() throws RecognitionException {
		EnumdeclContext _localctx = new EnumdeclContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_enumdecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(319);
			match(ENUM);
			setState(320);
			identifier();
			setState(321);
			match(T__10);
			setState(322);
			enumoptions();
			setState(323);
			match(T__11);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EnumoptionsContext extends ParserRuleContext {
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public EnumoptionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_enumoptions; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterEnumoptions(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitEnumoptions(this);
		}
	}

	public final EnumoptionsContext enumoptions() throws RecognitionException {
		EnumoptionsContext _localctx = new EnumoptionsContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_enumoptions);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(325);
			identifier();
			setState(330);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(326);
					match(T__5);
					setState(327);
					identifier();
					}
					} 
				}
				setState(332);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			}
			setState(334);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(333);
				match(T__5);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StructdeclContext extends ParserRuleContext {
		public TerminalNode STRUCT() { return getToken(UnrealScriptParser.STRUCT, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public StructbodyContext structbody() {
			return getRuleContext(StructbodyContext.class,0);
		}
		public List<StructparamsContext> structparams() {
			return getRuleContexts(StructparamsContext.class);
		}
		public StructparamsContext structparams(int i) {
			return getRuleContext(StructparamsContext.class,i);
		}
		public TerminalNode EXTENDS() { return getToken(UnrealScriptParser.EXTENDS, 0); }
		public PackageidentifierContext packageidentifier() {
			return getRuleContext(PackageidentifierContext.class,0);
		}
		public StructdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structdecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterStructdecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitStructdecl(this);
		}
	}

	public final StructdeclContext structdecl() throws RecognitionException {
		StructdeclContext _localctx = new StructdeclContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_structdecl);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(336);
			match(STRUCT);
			setState(340);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(337);
					structparams();
					}
					} 
				}
				setState(342);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			}
			setState(343);
			identifier();
			setState(346);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EXTENDS) {
				{
				setState(344);
				match(EXTENDS);
				setState(345);
				packageidentifier();
				}
			}

			setState(348);
			match(T__10);
			setState(349);
			structbody();
			setState(350);
			match(T__11);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StructparamsContext extends ParserRuleContext {
		public TerminalNode NATIVE() { return getToken(UnrealScriptParser.NATIVE, 0); }
		public TerminalNode EXPORT() { return getToken(UnrealScriptParser.EXPORT, 0); }
		public TerminalNode CONSTRUCTIVE() { return getToken(UnrealScriptParser.CONSTRUCTIVE, 0); }
		public StructparamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structparams; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterStructparams(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitStructparams(this);
		}
	}

	public final StructparamsContext structparams() throws RecognitionException {
		StructparamsContext _localctx = new StructparamsContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_structparams);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(352);
			_la = _input.LA(1);
			if ( !(((((_la - 77)) & ~0x3f) == 0 && ((1L << (_la - 77)) & 274878431233L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StructbodyContext extends ParserRuleContext {
		public List<VardeclContext> vardecl() {
			return getRuleContexts(VardeclContext.class);
		}
		public VardeclContext vardecl(int i) {
			return getRuleContext(VardeclContext.class,i);
		}
		public StructbodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structbody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterStructbody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitStructbody(this);
		}
	}

	public final StructbodyContext structbody() throws RecognitionException {
		StructbodyContext _localctx = new StructbodyContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_structbody);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(359);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(354);
				vardecl();
				setState(355);
				match(T__0);
				}
				}
				setState(361);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReplicationblockContext extends ParserRuleContext {
		public TerminalNode REPLICATION() { return getToken(UnrealScriptParser.REPLICATION, 0); }
		public List<ReplicationbodyContext> replicationbody() {
			return getRuleContexts(ReplicationbodyContext.class);
		}
		public ReplicationbodyContext replicationbody(int i) {
			return getRuleContext(ReplicationbodyContext.class,i);
		}
		public ReplicationblockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_replicationblock; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterReplicationblock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitReplicationblock(this);
		}
	}

	public final ReplicationblockContext replicationblock() throws RecognitionException {
		ReplicationblockContext _localctx = new ReplicationblockContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_replicationblock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(362);
			match(REPLICATION);
			setState(363);
			match(T__10);
			setState(367);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==RELIABLE || _la==UNRELIABLE) {
				{
				{
				setState(364);
				replicationbody();
				}
				}
				setState(369);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(370);
			match(T__11);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReplicationbodyContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(UnrealScriptParser.IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public TerminalNode RELIABLE() { return getToken(UnrealScriptParser.RELIABLE, 0); }
		public TerminalNode UNRELIABLE() { return getToken(UnrealScriptParser.UNRELIABLE, 0); }
		public ReplicationbodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_replicationbody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterReplicationbody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitReplicationbody(this);
		}
	}

	public final ReplicationbodyContext replicationbody() throws RecognitionException {
		ReplicationbodyContext _localctx = new ReplicationbodyContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_replicationbody);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(372);
			_la = _input.LA(1);
			if ( !(_la==RELIABLE || _la==UNRELIABLE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(373);
			match(IF);
			setState(374);
			match(T__1);
			setState(375);
			expression(0);
			setState(376);
			match(T__2);
			setState(377);
			identifier();
			setState(382);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(378);
				match(T__5);
				setState(379);
				identifier();
				}
				}
				setState(384);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(385);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BodyContext extends ParserRuleContext {
		public List<StatedeclContext> statedecl() {
			return getRuleContexts(StatedeclContext.class);
		}
		public StatedeclContext statedecl(int i) {
			return getRuleContext(StatedeclContext.class,i);
		}
		public List<FunctiondeclContext> functiondecl() {
			return getRuleContexts(FunctiondeclContext.class);
		}
		public FunctiondeclContext functiondecl(int i) {
			return getRuleContext(FunctiondeclContext.class,i);
		}
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitBody(this);
		}
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_body);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(389); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					setState(389);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
					case 1:
						{
						setState(387);
						statedecl();
						}
						break;
					case 2:
						{
						setState(388);
						functiondecl();
						}
						break;
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(391); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,29,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatedeclContext extends ParserRuleContext {
		public TerminalNode STATE() { return getToken(UnrealScriptParser.STATE, 0); }
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public StatebodyContext statebody() {
			return getRuleContext(StatebodyContext.class,0);
		}
		public List<StateparamsContext> stateparams() {
			return getRuleContexts(StateparamsContext.class);
		}
		public StateparamsContext stateparams(int i) {
			return getRuleContext(StateparamsContext.class,i);
		}
		public ConfiggroupContext configgroup() {
			return getRuleContext(ConfiggroupContext.class,0);
		}
		public TerminalNode EXTENDS() { return getToken(UnrealScriptParser.EXTENDS, 0); }
		public StatedeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statedecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterStatedecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitStatedecl(this);
		}
	}

	public final StatedeclContext statedecl() throws RecognitionException {
		StatedeclContext _localctx = new StatedeclContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_statedecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(396);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AUTO || _la==SIMULATED) {
				{
				{
				setState(393);
				stateparams();
				}
				}
				setState(398);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(399);
			match(STATE);
			setState(402);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(400);
				match(T__1);
				setState(401);
				match(T__2);
				}
			}

			setState(404);
			identifier();
			setState(406);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(405);
				configgroup();
				}
			}

			setState(410);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EXTENDS) {
				{
				setState(408);
				match(EXTENDS);
				setState(409);
				identifier();
				}
			}

			setState(412);
			statebody();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatebodyContext extends ParserRuleContext {
		public StatelabelsContext statelabels() {
			return getRuleContext(StatelabelsContext.class,0);
		}
		public StateignoreContext stateignore() {
			return getRuleContext(StateignoreContext.class,0);
		}
		public List<FunctiondeclContext> functiondecl() {
			return getRuleContexts(FunctiondeclContext.class);
		}
		public FunctiondeclContext functiondecl(int i) {
			return getRuleContext(FunctiondeclContext.class,i);
		}
		public StatebodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statebody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterStatebody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitStatebody(this);
		}
	}

	public final StatebodyContext statebody() throws RecognitionException {
		StatebodyContext _localctx = new StatebodyContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_statebody);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(414);
			match(T__10);
			setState(416);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
			case 1:
				{
				setState(415);
				stateignore();
				}
				break;
			}
			setState(421);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,35,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(418);
					functiondecl();
					}
					} 
				}
				setState(423);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,35,_ctx);
			}
			setState(424);
			statelabels();
			setState(425);
			match(T__11);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StateignoreContext extends ParserRuleContext {
		public TerminalNode IGNORES() { return getToken(UnrealScriptParser.IGNORES, 0); }
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public StateignoreContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stateignore; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterStateignore(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitStateignore(this);
		}
	}

	public final StateignoreContext stateignore() throws RecognitionException {
		StateignoreContext _localctx = new StateignoreContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_stateignore);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(427);
			match(IGNORES);
			setState(428);
			identifier();
			setState(433);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(429);
				match(T__5);
				setState(430);
				identifier();
				}
				}
				setState(435);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(436);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatelabelsContext extends ParserRuleContext {
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public StatelabelsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statelabels; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterStatelabels(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitStatelabels(this);
		}
	}

	public final StatelabelsContext statelabels() throws RecognitionException {
		StatelabelsContext _localctx = new StatelabelsContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_statelabels);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(448);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & -1L) != 0) || ((((_la - 129)) & ~0x3f) == 0 && ((1L << (_la - 129)) & 16777215L) != 0)) {
				{
				{
				setState(438);
				identifier();
				setState(439);
				match(T__12);
				setState(443);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,37,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(440);
						statement();
						}
						} 
					}
					setState(445);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,37,_ctx);
				}
				}
				}
				setState(450);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StateparamsContext extends ParserRuleContext {
		public TerminalNode AUTO() { return getToken(UnrealScriptParser.AUTO, 0); }
		public TerminalNode SIMULATED() { return getToken(UnrealScriptParser.SIMULATED, 0); }
		public StateparamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stateparams; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterStateparams(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitStateparams(this);
		}
	}

	public final StateparamsContext stateparams() throws RecognitionException {
		StateparamsContext _localctx = new StateparamsContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_stateparams);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(451);
			_la = _input.LA(1);
			if ( !(_la==AUTO || _la==SIMULATED) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctiondeclContext extends ParserRuleContext {
		public NormalfuncContext normalfunc() {
			return getRuleContext(NormalfuncContext.class,0);
		}
		public OperatorfuncContext operatorfunc() {
			return getRuleContext(OperatorfuncContext.class,0);
		}
		public FunctiondeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functiondecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterFunctiondecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitFunctiondecl(this);
		}
	}

	public final FunctiondeclContext functiondecl() throws RecognitionException {
		FunctiondeclContext _localctx = new FunctiondeclContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_functiondecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(455);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,39,_ctx) ) {
			case 1:
				{
				setState(453);
				normalfunc();
				}
				break;
			case 2:
				{
				setState(454);
				operatorfunc();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NormalfuncContext extends ParserRuleContext {
		public FunctiontypeContext functiontype() {
			return getRuleContext(FunctiontypeContext.class,0);
		}
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public List<FunctionparamsContext> functionparams() {
			return getRuleContexts(FunctionparamsContext.class);
		}
		public FunctionparamsContext functionparams(int i) {
			return getRuleContext(FunctionparamsContext.class,i);
		}
		public LocaltypeContext localtype() {
			return getRuleContext(LocaltypeContext.class,0);
		}
		public List<FunctionargsContext> functionargs() {
			return getRuleContexts(FunctionargsContext.class);
		}
		public FunctionargsContext functionargs(int i) {
			return getRuleContext(FunctionargsContext.class,i);
		}
		public FunctionbodyContext functionbody() {
			return getRuleContext(FunctionbodyContext.class,0);
		}
		public NormalfuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_normalfunc; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterNormalfunc(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitNormalfunc(this);
		}
	}

	public final NormalfuncContext normalfunc() throws RecognitionException {
		NormalfuncContext _localctx = new NormalfuncContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_normalfunc);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(460);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 95)) & ~0x3f) == 0 && ((1L << (_la - 95)) & 83614424465425L) != 0)) {
				{
				{
				setState(457);
				functionparams();
				}
				}
				setState(462);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(463);
			functiontype();
			setState(465);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,41,_ctx) ) {
			case 1:
				{
				setState(464);
				localtype();
				}
				break;
			}
			setState(467);
			identifier();
			setState(468);
			match(T__1);
			setState(477);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & -1L) != 0) || ((((_la - 129)) & ~0x3f) == 0 && ((1L << (_la - 129)) & 16777215L) != 0)) {
				{
				setState(469);
				functionargs();
				setState(474);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__5) {
					{
					{
					setState(470);
					match(T__5);
					setState(471);
					functionargs();
					}
					}
					setState(476);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(479);
			match(T__2);
			setState(484);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__10) {
				{
				setState(480);
				match(T__10);
				setState(481);
				functionbody();
				setState(482);
				match(T__11);
				}
			}

			setState(487);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__0) {
				{
				setState(486);
				match(T__0);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctiontypeContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(UnrealScriptParser.FUNCTION, 0); }
		public TerminalNode EVENT() { return getToken(UnrealScriptParser.EVENT, 0); }
		public TerminalNode DELEGATE() { return getToken(UnrealScriptParser.DELEGATE, 0); }
		public FunctiontypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functiontype; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterFunctiontype(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitFunctiontype(this);
		}
	}

	public final FunctiontypeContext functiontype() throws RecognitionException {
		FunctiontypeContext _localctx = new FunctiontypeContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_functiontype);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(489);
			_la = _input.LA(1);
			if ( !(((((_la - 80)) & ~0x3f) == 0 && ((1L << (_la - 80)) & 8404993L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionparamsContext extends ParserRuleContext {
		public ConstfuncparamsContext constfuncparams() {
			return getRuleContext(ConstfuncparamsContext.class,0);
		}
		public TerminalNode NATIVE() { return getToken(UnrealScriptParser.NATIVE, 0); }
		public TerminalNode IntVal() { return getToken(UnrealScriptParser.IntVal, 0); }
		public FunctionparamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionparams; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterFunctionparams(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitFunctionparams(this);
		}
	}

	public final FunctionparamsContext functionparams() throws RecognitionException {
		FunctionparamsContext _localctx = new FunctionparamsContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_functionparams);
		int _la;
		try {
			setState(498);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EXEC:
			case FINAL:
			case ITERATOR:
			case LATENT:
			case PRIVATE:
			case PROTECTED:
			case SIMULATED:
			case SINGULAR:
			case STATIC:
				enterOuterAlt(_localctx, 1);
				{
				setState(491);
				constfuncparams();
				}
				break;
			case NATIVE:
				enterOuterAlt(_localctx, 2);
				{
				setState(492);
				match(NATIVE);
				setState(496);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__1) {
					{
					setState(493);
					match(T__1);
					setState(494);
					match(IntVal);
					setState(495);
					match(T__2);
					}
				}

				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstfuncparamsContext extends ParserRuleContext {
		public TerminalNode FINAL() { return getToken(UnrealScriptParser.FINAL, 0); }
		public TerminalNode ITERATOR() { return getToken(UnrealScriptParser.ITERATOR, 0); }
		public TerminalNode LATENT() { return getToken(UnrealScriptParser.LATENT, 0); }
		public TerminalNode SIMULATED() { return getToken(UnrealScriptParser.SIMULATED, 0); }
		public TerminalNode SINGULAR() { return getToken(UnrealScriptParser.SINGULAR, 0); }
		public TerminalNode STATIC() { return getToken(UnrealScriptParser.STATIC, 0); }
		public TerminalNode EXEC() { return getToken(UnrealScriptParser.EXEC, 0); }
		public TerminalNode PROTECTED() { return getToken(UnrealScriptParser.PROTECTED, 0); }
		public TerminalNode PRIVATE() { return getToken(UnrealScriptParser.PRIVATE, 0); }
		public ConstfuncparamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constfuncparams; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterConstfuncparams(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitConstfuncparams(this);
		}
	}

	public final ConstfuncparamsContext constfuncparams() throws RecognitionException {
		ConstfuncparamsContext _localctx = new ConstfuncparamsContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_constfuncparams);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(500);
			_la = _input.LA(1);
			if ( !(((((_la - 95)) & ~0x3f) == 0 && ((1L << (_la - 95)) & 83614423416849L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperatorfuncContext extends ParserRuleContext {
		public OperatortypeContext operatortype() {
			return getRuleContext(OperatortypeContext.class,0);
		}
		public List<FunctionparamsContext> functionparams() {
			return getRuleContexts(FunctionparamsContext.class);
		}
		public FunctionparamsContext functionparams(int i) {
			return getRuleContext(FunctionparamsContext.class,i);
		}
		public FunctionbodyContext functionbody() {
			return getRuleContext(FunctionbodyContext.class,0);
		}
		public OperatorfuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operatorfunc; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterOperatorfunc(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitOperatorfunc(this);
		}
	}

	public final OperatorfuncContext operatorfunc() throws RecognitionException {
		OperatorfuncContext _localctx = new OperatorfuncContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_operatorfunc);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(505);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 95)) & ~0x3f) == 0 && ((1L << (_la - 95)) & 83614424465425L) != 0)) {
				{
				{
				setState(502);
				functionparams();
				}
				}
				setState(507);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(508);
			operatortype();
			setState(513);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__10) {
				{
				setState(509);
				match(T__10);
				setState(510);
				functionbody();
				setState(511);
				match(T__11);
				}
			}

			setState(516);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__0) {
				{
				setState(515);
				match(T__0);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperatortypeContext extends ParserRuleContext {
		public BinaryoperatorContext binaryoperator() {
			return getRuleContext(BinaryoperatorContext.class,0);
		}
		public UnaryoperatorContext unaryoperator() {
			return getRuleContext(UnaryoperatorContext.class,0);
		}
		public OperatortypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operatortype; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterOperatortype(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitOperatortype(this);
		}
	}

	public final OperatortypeContext operatortype() throws RecognitionException {
		OperatortypeContext _localctx = new OperatortypeContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_operatortype);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(520);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPERATOR:
				{
				setState(518);
				binaryoperator();
				}
				break;
			case POSTOPERATOR:
			case PREOPERATOR:
				{
				setState(519);
				unaryoperator();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinaryoperatorContext extends ParserRuleContext {
		public TerminalNode OPERATOR() { return getToken(UnrealScriptParser.OPERATOR, 0); }
		public TerminalNode IntVal() { return getToken(UnrealScriptParser.IntVal, 0); }
		public LocaltypeContext localtype() {
			return getRuleContext(LocaltypeContext.class,0);
		}
		public OpidentifierContext opidentifier() {
			return getRuleContext(OpidentifierContext.class,0);
		}
		public List<FunctionargsContext> functionargs() {
			return getRuleContexts(FunctionargsContext.class);
		}
		public FunctionargsContext functionargs(int i) {
			return getRuleContext(FunctionargsContext.class,i);
		}
		public BinaryoperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binaryoperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterBinaryoperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitBinaryoperator(this);
		}
	}

	public final BinaryoperatorContext binaryoperator() throws RecognitionException {
		BinaryoperatorContext _localctx = new BinaryoperatorContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_binaryoperator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(522);
			match(OPERATOR);
			setState(523);
			match(T__1);
			setState(524);
			match(IntVal);
			setState(525);
			match(T__2);
			setState(526);
			localtype();
			setState(527);
			opidentifier();
			setState(528);
			match(T__1);
			setState(529);
			functionargs();
			setState(530);
			match(T__5);
			setState(531);
			functionargs();
			setState(532);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnaryoperatorContext extends ParserRuleContext {
		public LocaltypeContext localtype() {
			return getRuleContext(LocaltypeContext.class,0);
		}
		public OpidentifierContext opidentifier() {
			return getRuleContext(OpidentifierContext.class,0);
		}
		public FunctionargsContext functionargs() {
			return getRuleContext(FunctionargsContext.class,0);
		}
		public TerminalNode PREOPERATOR() { return getToken(UnrealScriptParser.PREOPERATOR, 0); }
		public TerminalNode POSTOPERATOR() { return getToken(UnrealScriptParser.POSTOPERATOR, 0); }
		public UnaryoperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryoperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterUnaryoperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitUnaryoperator(this);
		}
	}

	public final UnaryoperatorContext unaryoperator() throws RecognitionException {
		UnaryoperatorContext _localctx = new UnaryoperatorContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_unaryoperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(534);
			_la = _input.LA(1);
			if ( !(_la==POSTOPERATOR || _la==PREOPERATOR) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(535);
			localtype();
			setState(536);
			opidentifier();
			setState(537);
			match(T__1);
			setState(538);
			functionargs();
			setState(539);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpidentifierContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public OperatornamesContext operatornames() {
			return getRuleContext(OperatornamesContext.class,0);
		}
		public OpidentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opidentifier; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterOpidentifier(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitOpidentifier(this);
		}
	}

	public final OpidentifierContext opidentifier() throws RecognitionException {
		OpidentifierContext _localctx = new OpidentifierContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_opidentifier);
		try {
			setState(543);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ABSTRACT:
			case ARRAY:
			case ASSERT:
			case AUTO:
			case BOOL:
			case BYTE:
			case CASE:
			case CLASS:
			case COERCE:
			case COLLAPSECATEGORIES:
			case CONFIG:
			case CONST:
			case CONSTRUCTIVE:
			case DEFAULT:
			case DEFAULTPROPERTIES:
			case DELEGATE:
			case DEPENDSON:
			case DEPRECATED:
			case DO:
			case DONTCOLLAPSECATEGORIES:
			case DYNAMICRECOMPILE:
			case EDFINDABLE:
			case EDITCONST:
			case EDITINLINE:
			case EDITINLINENEW:
			case EDITINLINENOTIFY:
			case EDITINLINEUSE:
			case ELSE:
			case ENUM:
			case EVENT:
			case EXEC:
			case EXPORT:
			case EXPORTSTRUCTS:
			case EXTENDS:
			case FINAL:
			case FLOAT:
			case FOR:
			case FOREACH:
			case FUNCTION:
			case GLOBALCONFIG:
			case HIDECATEGORIES:
			case IF:
			case IGNORES:
			case INPUT:
			case INT:
			case ITERATOR:
			case LATENT:
			case LOCAL:
			case LOCALIZED:
			case NAME:
			case NATIVE:
			case NATIVEREPLICATION:
			case NEW:
			case NOEXPORT:
			case NONATIVEREPLICATION:
			case NOTEDITINLINENEW:
			case NOTPLACEABLE:
			case OPERATOR:
			case OPTIONAL:
			case OUT:
			case PEROBJECTCONFIG:
			case PLACEABLE:
			case POSTOPERATOR:
			case PREOPERATOR:
			case PRIVATE:
			case PROTECTED:
			case RELIABLE:
			case REPLICATION:
			case RETURN:
			case SAFEREPLACE:
			case SELF:
			case SHOWCATEGORIES:
			case SIMULATED:
			case SINGULAR:
			case SKIP_:
			case STATE:
			case STATIC:
			case STRING:
			case STRUCT:
			case SWITCH:
			case TRANSIENT:
			case TRAVEL:
			case UNRELIABLE:
			case UNTIL:
			case VAR:
			case WHILE:
			case WITHIN:
			case IDENT:
				enterOuterAlt(_localctx, 1);
				{
				setState(541);
				identifier();
				}
				break;
			case T__4:
			case T__8:
			case T__9:
			case T__12:
			case T__13:
			case T__14:
			case T__15:
			case T__16:
			case T__17:
			case T__18:
			case T__19:
			case T__20:
			case T__21:
			case T__22:
			case T__23:
			case T__24:
			case T__25:
			case T__26:
			case T__27:
			case T__28:
			case T__29:
			case T__30:
			case T__31:
			case T__32:
			case T__33:
			case T__34:
			case T__35:
			case T__36:
			case T__37:
			case T__38:
			case T__39:
			case T__40:
			case T__41:
			case T__42:
			case T__43:
			case T__44:
			case T__45:
			case T__46:
			case T__47:
			case T__48:
				enterOuterAlt(_localctx, 2);
				{
				setState(542);
				operatornames();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperatornamesContext extends ParserRuleContext {
		public OperatornamesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operatornames; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterOperatornames(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitOperatornames(this);
		}
	}

	public final OperatornamesContext operatornames() throws RecognitionException {
		OperatornamesContext _localctx = new OperatornamesContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_operatornames);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(545);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1125899906836000L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionargsContext extends ParserRuleContext {
		public FunctionargtypeContext functionargtype() {
			return getRuleContext(FunctionargtypeContext.class,0);
		}
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public List<TerminalNode> OPTIONAL() { return getTokens(UnrealScriptParser.OPTIONAL); }
		public TerminalNode OPTIONAL(int i) {
			return getToken(UnrealScriptParser.OPTIONAL, i);
		}
		public List<TerminalNode> OUT() { return getTokens(UnrealScriptParser.OUT); }
		public TerminalNode OUT(int i) {
			return getToken(UnrealScriptParser.OUT, i);
		}
		public List<TerminalNode> COERCE() { return getTokens(UnrealScriptParser.COERCE); }
		public TerminalNode COERCE(int i) {
			return getToken(UnrealScriptParser.COERCE, i);
		}
		public List<TerminalNode> SKIP_() { return getTokens(UnrealScriptParser.SKIP_); }
		public TerminalNode SKIP_(int i) {
			return getToken(UnrealScriptParser.SKIP_, i);
		}
		public FunctionargsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionargs; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterFunctionargs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitFunctionargs(this);
		}
	}

	public final FunctionargsContext functionargs() throws RecognitionException {
		FunctionargsContext _localctx = new FunctionargsContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_functionargs);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(550);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,53,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(547);
					_la = _input.LA(1);
					if ( !(((((_la - 73)) & ~0x3f) == 0 && ((1L << (_la - 73)) & 3377699720527873L) != 0) || _la==SKIP_) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					} 
				}
				setState(552);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,53,_ctx);
			}
			setState(553);
			functionargtype();
			setState(554);
			identifier();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionargtypeContext extends ParserRuleContext {
		public ArraydeclContext arraydecl() {
			return getRuleContext(ArraydeclContext.class,0);
		}
		public DynarraydeclContext dynarraydecl() {
			return getRuleContext(DynarraydeclContext.class,0);
		}
		public PackageidentifierContext packageidentifier() {
			return getRuleContext(PackageidentifierContext.class,0);
		}
		public ClasstypeContext classtype() {
			return getRuleContext(ClasstypeContext.class,0);
		}
		public BasictypeContext basictype() {
			return getRuleContext(BasictypeContext.class,0);
		}
		public FunctionargtypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionargtype; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterFunctionargtype(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitFunctionargtype(this);
		}
	}

	public final FunctionargtypeContext functionargtype() throws RecognitionException {
		FunctionargtypeContext _localctx = new FunctionargtypeContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_functionargtype);
		try {
			setState(561);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,54,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(556);
				arraydecl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(557);
				dynarraydecl();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(558);
				packageidentifier();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(559);
				classtype();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(560);
				basictype();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionbodyContext extends ParserRuleContext {
		public List<LocaldeclContext> localdecl() {
			return getRuleContexts(LocaldeclContext.class);
		}
		public LocaldeclContext localdecl(int i) {
			return getRuleContext(LocaldeclContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public FunctionbodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionbody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterFunctionbody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitFunctionbody(this);
		}
	}

	public final FunctionbodyContext functionbody() throws RecognitionException {
		FunctionbodyContext _localctx = new FunctionbodyContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_functionbody);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(566);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,55,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(563);
					localdecl();
					}
					} 
				}
				setState(568);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,55,_ctx);
			}
			setState(572);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & -288230273047281658L) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & -1L) != 0) || ((((_la - 128)) & ~0x3f) == 0 && ((1L << (_la - 128)) & 33554431L) != 0)) {
				{
				{
				setState(569);
				statement();
				}
				}
				setState(574);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LocaldeclContext extends ParserRuleContext {
		public TerminalNode LOCAL() { return getToken(UnrealScriptParser.LOCAL, 0); }
		public LocaltypeContext localtype() {
			return getRuleContext(LocaltypeContext.class,0);
		}
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public List<ArrayindexContext> arrayindex() {
			return getRuleContexts(ArrayindexContext.class);
		}
		public ArrayindexContext arrayindex(int i) {
			return getRuleContext(ArrayindexContext.class,i);
		}
		public LocaldeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_localdecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterLocaldecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitLocaldecl(this);
		}
	}

	public final LocaldeclContext localdecl() throws RecognitionException {
		LocaldeclContext _localctx = new LocaldeclContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_localdecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(575);
			match(LOCAL);
			setState(576);
			localtype();
			setState(577);
			identifier();
			setState(579);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__6) {
				{
				setState(578);
				arrayindex();
				}
			}

			setState(588);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(581);
				match(T__5);
				setState(582);
				identifier();
				setState(584);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__6) {
					{
					setState(583);
					arrayindex();
					}
				}

				}
				}
				setState(590);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(591);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LocaltypeContext extends ParserRuleContext {
		public PackageidentifierContext packageidentifier() {
			return getRuleContext(PackageidentifierContext.class,0);
		}
		public ArraydeclContext arraydecl() {
			return getRuleContext(ArraydeclContext.class,0);
		}
		public DynarraydeclContext dynarraydecl() {
			return getRuleContext(DynarraydeclContext.class,0);
		}
		public ClasstypeContext classtype() {
			return getRuleContext(ClasstypeContext.class,0);
		}
		public BasictypeContext basictype() {
			return getRuleContext(BasictypeContext.class,0);
		}
		public LocaltypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_localtype; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterLocaltype(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitLocaltype(this);
		}
	}

	public final LocaltypeContext localtype() throws RecognitionException {
		LocaltypeContext _localctx = new LocaltypeContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_localtype);
		try {
			setState(598);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,60,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(593);
				packageidentifier();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(594);
				arraydecl();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(595);
				dynarraydecl();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(596);
				classtype();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(597);
				basictype();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CodeblockContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public CodeblockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_codeblock; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterCodeblock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitCodeblock(this);
		}
	}

	public final CodeblockContext codeblock() throws RecognitionException {
		CodeblockContext _localctx = new CodeblockContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_codeblock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(609);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
			case T__1:
			case T__13:
			case T__14:
			case T__22:
			case T__23:
			case T__34:
			case T__35:
			case StringVal:
			case NameVal:
			case IntVal:
			case FloatVal:
			case BoolVal:
			case NoneVal:
			case VectVal:
			case ABSTRACT:
			case ARRAY:
			case ASSERT:
			case AUTO:
			case BOOL:
			case BYTE:
			case CASE:
			case CLASS:
			case COERCE:
			case COLLAPSECATEGORIES:
			case CONFIG:
			case CONST:
			case CONSTRUCTIVE:
			case DEFAULT:
			case DEFAULTPROPERTIES:
			case DELEGATE:
			case DEPENDSON:
			case DEPRECATED:
			case DO:
			case DONTCOLLAPSECATEGORIES:
			case DYNAMICRECOMPILE:
			case EDFINDABLE:
			case EDITCONST:
			case EDITINLINE:
			case EDITINLINENEW:
			case EDITINLINENOTIFY:
			case EDITINLINEUSE:
			case ELSE:
			case ENUM:
			case EVENT:
			case EXEC:
			case EXPORT:
			case EXPORTSTRUCTS:
			case EXTENDS:
			case FINAL:
			case FLOAT:
			case FOR:
			case FOREACH:
			case FUNCTION:
			case GLOBALCONFIG:
			case HIDECATEGORIES:
			case IF:
			case IGNORES:
			case INPUT:
			case INT:
			case ITERATOR:
			case LATENT:
			case LOCAL:
			case LOCALIZED:
			case NAME:
			case NATIVE:
			case NATIVEREPLICATION:
			case NEW:
			case NOEXPORT:
			case NONATIVEREPLICATION:
			case NOTEDITINLINENEW:
			case NOTPLACEABLE:
			case OPERATOR:
			case OPTIONAL:
			case OUT:
			case PEROBJECTCONFIG:
			case PLACEABLE:
			case POSTOPERATOR:
			case PREOPERATOR:
			case PRIVATE:
			case PROTECTED:
			case RELIABLE:
			case REPLICATION:
			case RETURN:
			case SAFEREPLACE:
			case SELF:
			case SHOWCATEGORIES:
			case SIMULATED:
			case SINGULAR:
			case SKIP_:
			case STATE:
			case STATIC:
			case STRING:
			case STRUCT:
			case SWITCH:
			case TRANSIENT:
			case TRAVEL:
			case UNRELIABLE:
			case UNTIL:
			case VAR:
			case WHILE:
			case WITHIN:
			case IDENT:
				{
				setState(600);
				statement();
				}
				break;
			case T__10:
				{
				{
				setState(601);
				match(T__10);
				setState(605);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & -288230273047281658L) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & -1L) != 0) || ((((_la - 128)) & ~0x3f) == 0 && ((1L << (_la - 128)) & 33554431L) != 0)) {
					{
					{
					setState(602);
					statement();
					}
					}
					setState(607);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(608);
				match(T__11);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public AssertionContext assertion() {
			return getRuleContext(AssertionContext.class,0);
		}
		public IfstatementContext ifstatement() {
			return getRuleContext(IfstatementContext.class,0);
		}
		public SwitchstatementContext switchstatement() {
			return getRuleContext(SwitchstatementContext.class,0);
		}
		public WhileloopContext whileloop() {
			return getRuleContext(WhileloopContext.class,0);
		}
		public DoloopContext doloop() {
			return getRuleContext(DoloopContext.class,0);
		}
		public ForeachloopContext foreachloop() {
			return getRuleContext(ForeachloopContext.class,0);
		}
		public ForloopContext forloop() {
			return getRuleContext(ForloopContext.class,0);
		}
		public ReturnstatementContext returnstatement() {
			return getRuleContext(ReturnstatementContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_statement);
		try {
			setState(623);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,63,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(611);
				match(T__0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(612);
				assertion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(613);
				ifstatement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(614);
				switchstatement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(615);
				whileloop();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(616);
				doloop();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(617);
				foreachloop();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(618);
				forloop();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(619);
				returnstatement();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(620);
				expression(0);
				setState(621);
				match(T__0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssertionContext extends ParserRuleContext {
		public TerminalNode ASSERT() { return getToken(UnrealScriptParser.ASSERT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssertionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assertion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterAssertion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitAssertion(this);
		}
	}

	public final AssertionContext assertion() throws RecognitionException {
		AssertionContext _localctx = new AssertionContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_assertion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(625);
			match(ASSERT);
			setState(626);
			expression(0);
			setState(627);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfstatementContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(UnrealScriptParser.IF, 0); }
		public ParExpressionContext parExpression() {
			return getRuleContext(ParExpressionContext.class,0);
		}
		public List<CodeblockContext> codeblock() {
			return getRuleContexts(CodeblockContext.class);
		}
		public CodeblockContext codeblock(int i) {
			return getRuleContext(CodeblockContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(UnrealScriptParser.ELSE, 0); }
		public IfstatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifstatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterIfstatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitIfstatement(this);
		}
	}

	public final IfstatementContext ifstatement() throws RecognitionException {
		IfstatementContext _localctx = new IfstatementContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_ifstatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(629);
			match(IF);
			setState(630);
			parExpression();
			setState(631);
			codeblock();
			setState(634);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,64,_ctx) ) {
			case 1:
				{
				setState(632);
				match(ELSE);
				setState(633);
				codeblock();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SwitchstatementContext extends ParserRuleContext {
		public TerminalNode SWITCH() { return getToken(UnrealScriptParser.SWITCH, 0); }
		public ParExpressionContext parExpression() {
			return getRuleContext(ParExpressionContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<CaseruleContext> caserule() {
			return getRuleContexts(CaseruleContext.class);
		}
		public CaseruleContext caserule(int i) {
			return getRuleContext(CaseruleContext.class,i);
		}
		public DefaultruleContext defaultrule() {
			return getRuleContext(DefaultruleContext.class,0);
		}
		public SwitchstatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switchstatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterSwitchstatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitSwitchstatement(this);
		}
	}

	public final SwitchstatementContext switchstatement() throws RecognitionException {
		SwitchstatementContext _localctx = new SwitchstatementContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_switchstatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(636);
			match(SWITCH);
			setState(639);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,65,_ctx) ) {
			case 1:
				{
				setState(637);
				parExpression();
				}
				break;
			case 2:
				{
				setState(638);
				expression(0);
				}
				break;
			}
			setState(641);
			match(T__10);
			setState(645);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CASE) {
				{
				{
				setState(642);
				caserule();
				}
				}
				setState(647);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(649);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DEFAULT) {
				{
				setState(648);
				defaultrule();
				}
			}

			setState(651);
			match(T__11);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileloopContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(UnrealScriptParser.WHILE, 0); }
		public ParExpressionContext parExpression() {
			return getRuleContext(ParExpressionContext.class,0);
		}
		public CodeblockContext codeblock() {
			return getRuleContext(CodeblockContext.class,0);
		}
		public WhileloopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileloop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterWhileloop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitWhileloop(this);
		}
	}

	public final WhileloopContext whileloop() throws RecognitionException {
		WhileloopContext _localctx = new WhileloopContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_whileloop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(653);
			match(WHILE);
			setState(654);
			parExpression();
			setState(655);
			codeblock();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DoloopContext extends ParserRuleContext {
		public TerminalNode DO() { return getToken(UnrealScriptParser.DO, 0); }
		public CodeblockContext codeblock() {
			return getRuleContext(CodeblockContext.class,0);
		}
		public TerminalNode UNTIL() { return getToken(UnrealScriptParser.UNTIL, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public DoloopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_doloop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterDoloop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitDoloop(this);
		}
	}

	public final DoloopContext doloop() throws RecognitionException {
		DoloopContext _localctx = new DoloopContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_doloop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(657);
			match(DO);
			setState(658);
			codeblock();
			setState(659);
			match(UNTIL);
			setState(660);
			match(T__1);
			setState(661);
			expression(0);
			setState(662);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForeachloopContext extends ParserRuleContext {
		public TerminalNode FOREACH() { return getToken(UnrealScriptParser.FOREACH, 0); }
		public QualifiedidentifierContext qualifiedidentifier() {
			return getRuleContext(QualifiedidentifierContext.class,0);
		}
		public CodeblockContext codeblock() {
			return getRuleContext(CodeblockContext.class,0);
		}
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public ForeachloopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_foreachloop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterForeachloop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitForeachloop(this);
		}
	}

	public final ForeachloopContext foreachloop() throws RecognitionException {
		ForeachloopContext _localctx = new ForeachloopContext(_ctx, getState());
		enterRule(_localctx, 114, RULE_foreachloop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(664);
			match(FOREACH);
			setState(665);
			qualifiedidentifier();
			setState(666);
			match(T__1);
			setState(668);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & -288230273047281596L) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & -1L) != 0) || ((((_la - 128)) & ~0x3f) == 0 && ((1L << (_la - 128)) & 33554431L) != 0)) {
				{
				setState(667);
				expressionList();
				}
			}

			setState(670);
			match(T__2);
			setState(671);
			codeblock();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForloopContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(UnrealScriptParser.FOR, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public CodeblockContext codeblock() {
			return getRuleContext(CodeblockContext.class,0);
		}
		public ForloopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forloop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterForloop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitForloop(this);
		}
	}

	public final ForloopContext forloop() throws RecognitionException {
		ForloopContext _localctx = new ForloopContext(_ctx, getState());
		enterRule(_localctx, 116, RULE_forloop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(673);
			match(FOR);
			setState(674);
			match(T__1);
			setState(675);
			identifier();
			setState(676);
			match(T__4);
			setState(677);
			expression(0);
			setState(678);
			match(T__0);
			setState(679);
			expression(0);
			setState(680);
			match(T__0);
			setState(681);
			expression(0);
			setState(682);
			match(T__2);
			setState(684);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,69,_ctx) ) {
			case 1:
				{
				setState(683);
				codeblock();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnstatementContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(UnrealScriptParser.RETURN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ReturnstatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnstatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterReturnstatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitReturnstatement(this);
		}
	}

	public final ReturnstatementContext returnstatement() throws RecognitionException {
		ReturnstatementContext _localctx = new ReturnstatementContext(_ctx, getState());
		enterRule(_localctx, 118, RULE_returnstatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(686);
			match(RETURN);
			setState(688);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & -288230273047281660L) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & -1L) != 0) || ((((_la - 128)) & ~0x3f) == 0 && ((1L << (_la - 128)) & 33554431L) != 0)) {
				{
				setState(687);
				expression(0);
				}
			}

			setState(690);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CaseruleContext extends ParserRuleContext {
		public TerminalNode CASE() { return getToken(UnrealScriptParser.CASE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public CasecodeblockContext casecodeblock() {
			return getRuleContext(CasecodeblockContext.class,0);
		}
		public CaseruleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_caserule; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterCaserule(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitCaserule(this);
		}
	}

	public final CaseruleContext caserule() throws RecognitionException {
		CaseruleContext _localctx = new CaseruleContext(_ctx, getState());
		enterRule(_localctx, 120, RULE_caserule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(692);
			match(CASE);
			setState(693);
			expression(0);
			setState(694);
			match(T__12);
			setState(695);
			casecodeblock();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CasecodeblockContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public CasecodeblockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_casecodeblock; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterCasecodeblock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitCasecodeblock(this);
		}
	}

	public final CasecodeblockContext casecodeblock() throws RecognitionException {
		CasecodeblockContext _localctx = new CasecodeblockContext(_ctx, getState());
		enterRule(_localctx, 122, RULE_casecodeblock);
		int _la;
		try {
			int _alt;
			setState(711);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
			case T__1:
			case T__11:
			case T__13:
			case T__14:
			case T__22:
			case T__23:
			case T__34:
			case T__35:
			case StringVal:
			case NameVal:
			case IntVal:
			case FloatVal:
			case BoolVal:
			case NoneVal:
			case VectVal:
			case ABSTRACT:
			case ARRAY:
			case ASSERT:
			case AUTO:
			case BOOL:
			case BYTE:
			case CASE:
			case CLASS:
			case COERCE:
			case COLLAPSECATEGORIES:
			case CONFIG:
			case CONST:
			case CONSTRUCTIVE:
			case DEFAULT:
			case DEFAULTPROPERTIES:
			case DELEGATE:
			case DEPENDSON:
			case DEPRECATED:
			case DO:
			case DONTCOLLAPSECATEGORIES:
			case DYNAMICRECOMPILE:
			case EDFINDABLE:
			case EDITCONST:
			case EDITINLINE:
			case EDITINLINENEW:
			case EDITINLINENOTIFY:
			case EDITINLINEUSE:
			case ELSE:
			case ENUM:
			case EVENT:
			case EXEC:
			case EXPORT:
			case EXPORTSTRUCTS:
			case EXTENDS:
			case FINAL:
			case FLOAT:
			case FOR:
			case FOREACH:
			case FUNCTION:
			case GLOBALCONFIG:
			case HIDECATEGORIES:
			case IF:
			case IGNORES:
			case INPUT:
			case INT:
			case ITERATOR:
			case LATENT:
			case LOCAL:
			case LOCALIZED:
			case NAME:
			case NATIVE:
			case NATIVEREPLICATION:
			case NEW:
			case NOEXPORT:
			case NONATIVEREPLICATION:
			case NOTEDITINLINENEW:
			case NOTPLACEABLE:
			case OPERATOR:
			case OPTIONAL:
			case OUT:
			case PEROBJECTCONFIG:
			case PLACEABLE:
			case POSTOPERATOR:
			case PREOPERATOR:
			case PRIVATE:
			case PROTECTED:
			case RELIABLE:
			case REPLICATION:
			case RETURN:
			case SAFEREPLACE:
			case SELF:
			case SHOWCATEGORIES:
			case SIMULATED:
			case SINGULAR:
			case SKIP_:
			case STATE:
			case STATIC:
			case STRING:
			case STRUCT:
			case SWITCH:
			case TRANSIENT:
			case TRAVEL:
			case UNRELIABLE:
			case UNTIL:
			case VAR:
			case WHILE:
			case WITHIN:
			case IDENT:
				enterOuterAlt(_localctx, 1);
				{
				setState(700);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,71,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(697);
						statement();
						}
						} 
					}
					setState(702);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,71,_ctx);
				}
				}
				break;
			case T__10:
				enterOuterAlt(_localctx, 2);
				{
				{
				setState(703);
				match(T__10);
				setState(707);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & -288230273047281658L) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & -1L) != 0) || ((((_la - 128)) & ~0x3f) == 0 && ((1L << (_la - 128)) & 33554431L) != 0)) {
					{
					{
					setState(704);
					statement();
					}
					}
					setState(709);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(710);
				match(T__11);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DefaultruleContext extends ParserRuleContext {
		public TerminalNode DEFAULT() { return getToken(UnrealScriptParser.DEFAULT, 0); }
		public CasecodeblockContext casecodeblock() {
			return getRuleContext(CasecodeblockContext.class,0);
		}
		public DefaultruleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_defaultrule; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterDefaultrule(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitDefaultrule(this);
		}
	}

	public final DefaultruleContext defaultrule() throws RecognitionException {
		DefaultruleContext _localctx = new DefaultruleContext(_ctx, getState());
		enterRule(_localctx, 124, RULE_defaultrule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(713);
			match(DEFAULT);
			setState(714);
			match(T__12);
			setState(715);
			casecodeblock();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public PrimaryContext primary() {
			return getRuleContext(PrimaryContext.class,0);
		}
		public BasictypeContext basictype() {
			return getRuleContext(BasictypeContext.class,0);
		}
		public ExpressionListContext expressionList() {
			return getRuleContext(ExpressionListContext.class,0);
		}
		public TerminalNode NEW() { return getToken(UnrealScriptParser.NEW, 0); }
		public CreatorContext creator() {
			return getRuleContext(CreatorContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitExpression(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 126;
		enterRecursionRule(_localctx, 126, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(732);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,75,_ctx) ) {
			case 1:
				{
				setState(718);
				primary();
				}
				break;
			case 2:
				{
				setState(719);
				basictype();
				setState(720);
				match(T__1);
				setState(722);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & -288230273047281596L) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & -1L) != 0) || ((((_la - 128)) & ~0x3f) == 0 && ((1L << (_la - 128)) & 33554431L) != 0)) {
					{
					setState(721);
					expressionList();
					}
				}

				setState(724);
				match(T__2);
				}
				break;
			case 3:
				{
				setState(726);
				match(NEW);
				setState(727);
				creator();
				}
				break;
			case 4:
				{
				setState(728);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 103104380928L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(729);
				expression(19);
				}
				break;
			case 5:
				{
				setState(730);
				_la = _input.LA(1);
				if ( !(_la==T__13 || _la==T__14) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(731);
				expression(18);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(815);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,79,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(813);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,78,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(734);
						if (!(precpred(_ctx, 17))) throw new FailedPredicateException(this, "precpred(_ctx, 17)");
						setState(735);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 138936320L) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(736);
						expression(18);
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(737);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(738);
						_la = _input.LA(1);
						if ( !(_la==T__22 || _la==T__23) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(739);
						expression(17);
						}
						break;
					case 3:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(740);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(741);
						match(T__43);
						setState(742);
						expression(16);
						}
						break;
					case 4:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(743);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(744);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 562953174646784L) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(745);
						expression(15);
						}
						break;
					case 5:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(746);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(754);
						_errHandler.sync(this);
						switch ( getInterpreter().adaptivePredict(_input,76,_ctx) ) {
						case 1:
							{
							setState(747);
							match(T__8);
							setState(748);
							match(T__8);
							}
							break;
						case 2:
							{
							setState(749);
							match(T__9);
							setState(750);
							match(T__9);
							setState(751);
							match(T__9);
							}
							break;
						case 3:
							{
							setState(752);
							match(T__9);
							setState(753);
							match(T__9);
							}
							break;
						}
						setState(756);
						expression(14);
						}
						break;
					case 6:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(757);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(758);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 25769805312L) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(759);
						expression(13);
						}
						break;
					case 7:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(760);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(761);
						_la = _input.LA(1);
						if ( !(_la==T__31 || _la==T__44) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(762);
						expression(12);
						}
						break;
					case 8:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(763);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(764);
						identifier();
						setState(765);
						expression(11);
						}
						break;
					case 9:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(767);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(768);
						match(T__15);
						setState(769);
						expression(10);
						}
						break;
					case 10:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(770);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(771);
						match(T__17);
						setState(772);
						expression(9);
						}
						break;
					case 11:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(773);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(774);
						match(T__20);
						setState(775);
						expression(8);
						}
						break;
					case 12:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(776);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(777);
						match(T__19);
						setState(778);
						expression(7);
						}
						break;
					case 13:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(779);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(780);
						match(T__24);
						setState(781);
						expression(6);
						}
						break;
					case 14:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(782);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(783);
						match(T__41);
						setState(784);
						expression(5);
						}
						break;
					case 15:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(785);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(786);
						match(T__42);
						setState(787);
						expression(4);
						}
						break;
					case 16:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(788);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(789);
						match(T__27);
						setState(790);
						expression(0);
						setState(791);
						match(T__12);
						setState(792);
						expression(3);
						}
						break;
					case 17:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(794);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(795);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 143134148825972768L) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(796);
						expression(1);
						}
						break;
					case 18:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(797);
						if (!(precpred(_ctx, 25))) throw new FailedPredicateException(this, "precpred(_ctx, 25)");
						setState(798);
						match(T__3);
						setState(799);
						identifier();
						}
						break;
					case 19:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(800);
						if (!(precpred(_ctx, 24))) throw new FailedPredicateException(this, "precpred(_ctx, 24)");
						setState(801);
						match(T__6);
						setState(802);
						expression(0);
						setState(803);
						match(T__7);
						}
						break;
					case 20:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(805);
						if (!(precpred(_ctx, 23))) throw new FailedPredicateException(this, "precpred(_ctx, 23)");
						setState(806);
						match(T__1);
						setState(808);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & -288230273047281596L) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & -1L) != 0) || ((((_la - 128)) & ~0x3f) == 0 && ((1L << (_la - 128)) & 33554431L) != 0)) {
							{
							setState(807);
							expressionList();
							}
						}

						setState(810);
						match(T__2);
						}
						break;
					case 21:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(811);
						if (!(precpred(_ctx, 20))) throw new FailedPredicateException(this, "precpred(_ctx, 20)");
						setState(812);
						_la = _input.LA(1);
						if ( !(_la==T__34 || _la==T__35) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						}
						break;
					}
					} 
				}
				setState(817);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,79,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryContext extends ParserRuleContext {
		public ParExpressionContext parExpression() {
			return getRuleContext(ParExpressionContext.class,0);
		}
		public TerminalNode SELF() { return getToken(UnrealScriptParser.SELF, 0); }
		public ConstvalueContext constvalue() {
			return getRuleContext(ConstvalueContext.class,0);
		}
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public PrimaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterPrimary(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitPrimary(this);
		}
	}

	public final PrimaryContext primary() throws RecognitionException {
		PrimaryContext _localctx = new PrimaryContext(_ctx, getState());
		enterRule(_localctx, 128, RULE_primary);
		try {
			setState(822);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,80,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(818);
				parExpression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(819);
				match(SELF);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(820);
				constvalue();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(821);
				identifier();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CreatorContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public ClassvalContext classval() {
			return getRuleContext(ClassvalContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public CreatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_creator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterCreator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitCreator(this);
		}
	}

	public final CreatorContext creator() throws RecognitionException {
		CreatorContext _localctx = new CreatorContext(_ctx, getState());
		enterRule(_localctx, 130, RULE_creator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(836);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(824);
				match(T__1);
				setState(826);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & -288230273047281660L) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & -1L) != 0) || ((((_la - 128)) & ~0x3f) == 0 && ((1L << (_la - 128)) & 33554431L) != 0)) {
					{
					setState(825);
					expression(0);
					}
				}

				setState(832);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__5) {
					{
					{
					setState(828);
					match(T__5);
					setState(829);
					expression(0);
					}
					}
					setState(834);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(835);
				match(T__2);
				}
			}

			setState(840);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,84,_ctx) ) {
			case 1:
				{
				setState(838);
				identifier();
				}
				break;
			case 2:
				{
				setState(839);
				classval();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParExpressionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ParExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterParExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitParExpression(this);
		}
	}

	public final ParExpressionContext parExpression() throws RecognitionException {
		ParExpressionContext _localctx = new ParExpressionContext(_ctx, getState());
		enterRule(_localctx, 132, RULE_parExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(842);
			match(T__1);
			setState(843);
			expression(0);
			setState(844);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionListContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ExpressionListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterExpressionList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitExpressionList(this);
		}
	}

	public final ExpressionListContext expressionList() throws RecognitionException {
		ExpressionListContext _localctx = new ExpressionListContext(_ctx, getState());
		enterRule(_localctx, 134, RULE_expressionList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(847);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(846);
				match(T__5);
				}
			}

			setState(849);
			expression(0);
			setState(856);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(850);
				match(T__5);
				setState(852);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & -288230273047281660L) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & -1L) != 0) || ((((_la - 128)) & ~0x3f) == 0 && ((1L << (_la - 128)) & 33554431L) != 0)) {
					{
					setState(851);
					expression(0);
					}
				}

				}
				}
				setState(858);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DefaultpropertiesblockContext extends ParserRuleContext {
		public TerminalNode DEFAULTPROPERTIES() { return getToken(UnrealScriptParser.DEFAULTPROPERTIES, 0); }
		public List<DefpropContext> defprop() {
			return getRuleContexts(DefpropContext.class);
		}
		public DefpropContext defprop(int i) {
			return getRuleContext(DefpropContext.class,i);
		}
		public DefaultpropertiesblockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_defaultpropertiesblock; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterDefaultpropertiesblock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitDefaultpropertiesblock(this);
		}
	}

	public final DefaultpropertiesblockContext defaultpropertiesblock() throws RecognitionException {
		DefaultpropertiesblockContext _localctx = new DefaultpropertiesblockContext(_ctx, getState());
		enterRule(_localctx, 136, RULE_defaultpropertiesblock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(859);
			match(DEFAULTPROPERTIES);
			setState(860);
			match(T__10);
			setState(864);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & -1L) != 0) || ((((_la - 129)) & ~0x3f) == 0 && ((1L << (_la - 129)) & 16777215L) != 0)) {
				{
				{
				setState(861);
				defprop();
				}
				}
				setState(866);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(867);
			match(T__11);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DefpropContext extends ParserRuleContext {
		public DefpropidentifierContext defpropidentifier() {
			return getRuleContext(DefpropidentifierContext.class,0);
		}
		public ConstvalueContext constvalue() {
			return getRuleContext(ConstvalueContext.class,0);
		}
		public DefpropContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_defprop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterDefprop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitDefprop(this);
		}
	}

	public final DefpropContext defprop() throws RecognitionException {
		DefpropContext _localctx = new DefpropContext(_ctx, getState());
		enterRule(_localctx, 138, RULE_defprop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(869);
			defpropidentifier();
			setState(870);
			match(T__4);
			setState(871);
			constvalue();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DefpropidentifierContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode IntVal() { return getToken(UnrealScriptParser.IntVal, 0); }
		public DefpropidentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_defpropidentifier; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterDefpropidentifier(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitDefpropidentifier(this);
		}
	}

	public final DefpropidentifierContext defpropidentifier() throws RecognitionException {
		DefpropidentifierContext _localctx = new DefpropidentifierContext(_ctx, getState());
		enterRule(_localctx, 140, RULE_defpropidentifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(873);
			identifier();
			setState(880);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
				{
				{
				setState(874);
				match(T__1);
				setState(875);
				match(IntVal);
				setState(876);
				match(T__2);
				}
				}
				break;
			case T__6:
				{
				{
				setState(877);
				match(T__6);
				setState(878);
				match(IntVal);
				setState(879);
				match(T__7);
				}
				}
				break;
			case T__4:
				break;
			default:
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QualifiedidentifierContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(UnrealScriptParser.CLASS, 0); }
		public PackageidentifierContext packageidentifier() {
			return getRuleContext(PackageidentifierContext.class,0);
		}
		public TerminalNode DEFAULT() { return getToken(UnrealScriptParser.DEFAULT, 0); }
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public QualifiedidentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_qualifiedidentifier; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterQualifiedidentifier(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitQualifiedidentifier(this);
		}
	}

	public final QualifiedidentifierContext qualifiedidentifier() throws RecognitionException {
		QualifiedidentifierContext _localctx = new QualifiedidentifierContext(_ctx, getState());
		enterRule(_localctx, 142, RULE_qualifiedidentifier);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(900);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,91,_ctx) ) {
			case 1:
				{
				{
				setState(882);
				match(CLASS);
				setState(883);
				match(T__56);
				setState(884);
				packageidentifier();
				setState(885);
				match(T__56);
				setState(886);
				match(T__3);
				setState(887);
				match(DEFAULT);
				setState(888);
				match(T__3);
				setState(889);
				identifier();
				}
				}
				break;
			case 2:
				{
				{
				setState(896);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,90,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(891);
						identifier();
						setState(892);
						match(T__3);
						}
						} 
					}
					setState(898);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,90,_ctx);
				}
				setState(899);
				identifier();
				}
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdentifierlistContext extends ParserRuleContext {
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public IdentifierlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifierlist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).enterIdentifierlist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UnrealScriptListener ) ((UnrealScriptListener)listener).exitIdentifierlist(this);
		}
	}

	public final IdentifierlistContext identifierlist() throws RecognitionException {
		IdentifierlistContext _localctx = new IdentifierlistContext(_ctx, getState());
		enterRule(_localctx, 144, RULE_identifierlist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(902);
			identifier();
			setState(907);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(903);
				match(T__5);
				setState(904);
				identifier();
				}
				}
				setState(909);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 63:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 17);
		case 1:
			return precpred(_ctx, 16);
		case 2:
			return precpred(_ctx, 15);
		case 3:
			return precpred(_ctx, 14);
		case 4:
			return precpred(_ctx, 13);
		case 5:
			return precpred(_ctx, 12);
		case 6:
			return precpred(_ctx, 11);
		case 7:
			return precpred(_ctx, 10);
		case 8:
			return precpred(_ctx, 9);
		case 9:
			return precpred(_ctx, 8);
		case 10:
			return precpred(_ctx, 7);
		case 11:
			return precpred(_ctx, 6);
		case 12:
			return precpred(_ctx, 5);
		case 13:
			return precpred(_ctx, 4);
		case 14:
			return precpred(_ctx, 3);
		case 15:
			return precpred(_ctx, 2);
		case 16:
			return precpred(_ctx, 1);
		case 17:
			return precpred(_ctx, 25);
		case 18:
			return precpred(_ctx, 24);
		case 19:
			return precpred(_ctx, 23);
		case 20:
			return precpred(_ctx, 20);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u009c\u038f\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007"+
		"\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007"+
		"\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007"+
		"\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007"+
		"\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007"+
		"\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007"+
		"\"\u0002#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007"+
		"\'\u0002(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007+\u0002,\u0007"+
		",\u0002-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u00070\u00021\u0007"+
		"1\u00022\u00072\u00023\u00073\u00024\u00074\u00025\u00075\u00026\u0007"+
		"6\u00027\u00077\u00028\u00078\u00029\u00079\u0002:\u0007:\u0002;\u0007"+
		";\u0002<\u0007<\u0002=\u0007=\u0002>\u0007>\u0002?\u0007?\u0002@\u0007"+
		"@\u0002A\u0007A\u0002B\u0007B\u0002C\u0007C\u0002D\u0007D\u0002E\u0007"+
		"E\u0002F\u0007F\u0002G\u0007G\u0002H\u0007H\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0005\u0000\u0097\b\u0000\n\u0000\f\u0000\u009a\t\u0000"+
		"\u0001\u0000\u0003\u0000\u009d\b\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u0001\u00a3\b\u0001\u0001\u0001\u0005\u0001\u00a6\b"+
		"\u0001\n\u0001\f\u0001\u00a9\t\u0001\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0003\u0002\u00ba\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0003\u0002\u00c6\b\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005\u00cf\b\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006"+
		"\u00d7\b\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0003\b\u00e9\b\b\u0001\t\u0001\t\u0001\t\u0001"+
		"\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0003\u000b\u00f3\b\u000b\u0001"+
		"\u000b\u0005\u000b\u00f6\b\u000b\n\u000b\f\u000b\u00f9\t\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0003\u000b\u00fe\b\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0003\u000b\u0103\b\u000b\u0005\u000b\u0105\b\u000b\n\u000b"+
		"\f\u000b\u0108\t\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r"+
		"\u0001\u000e\u0001\u000e\u0003\u000e\u0112\b\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0003\u000f\u011d\b\u000f\u0001\u0010\u0001\u0010\u0001\u0011"+
		"\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u0126\b\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0005\u0013"+
		"\u012d\b\u0013\n\u0013\f\u0013\u0130\t\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0003\u0013\u0135\b\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014\u013e\b\u0014\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0005\u0016\u0149\b\u0016\n\u0016\f\u0016"+
		"\u014c\t\u0016\u0001\u0016\u0003\u0016\u014f\b\u0016\u0001\u0017\u0001"+
		"\u0017\u0005\u0017\u0153\b\u0017\n\u0017\f\u0017\u0156\t\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0003\u0017\u015b\b\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0005\u0019\u0166\b\u0019\n\u0019\f\u0019\u0169\t\u0019\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0005\u001a\u016e\b\u001a\n\u001a\f\u001a"+
		"\u0171\t\u001a\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001b"+
		"\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0005\u001b"+
		"\u017d\b\u001b\n\u001b\f\u001b\u0180\t\u001b\u0001\u001b\u0001\u001b\u0001"+
		"\u001c\u0001\u001c\u0004\u001c\u0186\b\u001c\u000b\u001c\f\u001c\u0187"+
		"\u0001\u001d\u0005\u001d\u018b\b\u001d\n\u001d\f\u001d\u018e\t\u001d\u0001"+
		"\u001d\u0001\u001d\u0001\u001d\u0003\u001d\u0193\b\u001d\u0001\u001d\u0001"+
		"\u001d\u0003\u001d\u0197\b\u001d\u0001\u001d\u0001\u001d\u0003\u001d\u019b"+
		"\b\u001d\u0001\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0003\u001e\u01a1"+
		"\b\u001e\u0001\u001e\u0005\u001e\u01a4\b\u001e\n\u001e\f\u001e\u01a7\t"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0005\u001f\u01b0\b\u001f\n\u001f\f\u001f\u01b3\t\u001f"+
		"\u0001\u001f\u0001\u001f\u0001 \u0001 \u0001 \u0005 \u01ba\b \n \f \u01bd"+
		"\t \u0005 \u01bf\b \n \f \u01c2\t \u0001!\u0001!\u0001\"\u0001\"\u0003"+
		"\"\u01c8\b\"\u0001#\u0005#\u01cb\b#\n#\f#\u01ce\t#\u0001#\u0001#\u0003"+
		"#\u01d2\b#\u0001#\u0001#\u0001#\u0001#\u0001#\u0005#\u01d9\b#\n#\f#\u01dc"+
		"\t#\u0003#\u01de\b#\u0001#\u0001#\u0001#\u0001#\u0001#\u0003#\u01e5\b"+
		"#\u0001#\u0003#\u01e8\b#\u0001$\u0001$\u0001%\u0001%\u0001%\u0001%\u0001"+
		"%\u0003%\u01f1\b%\u0003%\u01f3\b%\u0001&\u0001&\u0001\'\u0005\'\u01f8"+
		"\b\'\n\'\f\'\u01fb\t\'\u0001\'\u0001\'\u0001\'\u0001\'\u0001\'\u0003\'"+
		"\u0202\b\'\u0001\'\u0003\'\u0205\b\'\u0001(\u0001(\u0003(\u0209\b(\u0001"+
		")\u0001)\u0001)\u0001)\u0001)\u0001)\u0001)\u0001)\u0001)\u0001)\u0001"+
		")\u0001)\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001+\u0001"+
		"+\u0003+\u0220\b+\u0001,\u0001,\u0001-\u0005-\u0225\b-\n-\f-\u0228\t-"+
		"\u0001-\u0001-\u0001-\u0001.\u0001.\u0001.\u0001.\u0001.\u0003.\u0232"+
		"\b.\u0001/\u0005/\u0235\b/\n/\f/\u0238\t/\u0001/\u0005/\u023b\b/\n/\f"+
		"/\u023e\t/\u00010\u00010\u00010\u00010\u00030\u0244\b0\u00010\u00010\u0001"+
		"0\u00030\u0249\b0\u00050\u024b\b0\n0\f0\u024e\t0\u00010\u00010\u00011"+
		"\u00011\u00011\u00011\u00011\u00031\u0257\b1\u00012\u00012\u00012\u0005"+
		"2\u025c\b2\n2\f2\u025f\t2\u00012\u00032\u0262\b2\u00013\u00013\u00013"+
		"\u00013\u00013\u00013\u00013\u00013\u00013\u00013\u00013\u00013\u0003"+
		"3\u0270\b3\u00014\u00014\u00014\u00014\u00015\u00015\u00015\u00015\u0001"+
		"5\u00035\u027b\b5\u00016\u00016\u00016\u00036\u0280\b6\u00016\u00016\u0005"+
		"6\u0284\b6\n6\f6\u0287\t6\u00016\u00036\u028a\b6\u00016\u00016\u00017"+
		"\u00017\u00017\u00017\u00018\u00018\u00018\u00018\u00018\u00018\u0001"+
		"8\u00019\u00019\u00019\u00019\u00039\u029d\b9\u00019\u00019\u00019\u0001"+
		":\u0001:\u0001:\u0001:\u0001:\u0001:\u0001:\u0001:\u0001:\u0001:\u0001"+
		":\u0003:\u02ad\b:\u0001;\u0001;\u0003;\u02b1\b;\u0001;\u0001;\u0001<\u0001"+
		"<\u0001<\u0001<\u0001<\u0001=\u0005=\u02bb\b=\n=\f=\u02be\t=\u0001=\u0001"+
		"=\u0005=\u02c2\b=\n=\f=\u02c5\t=\u0001=\u0003=\u02c8\b=\u0001>\u0001>"+
		"\u0001>\u0001>\u0001?\u0001?\u0001?\u0001?\u0001?\u0003?\u02d3\b?\u0001"+
		"?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0003?\u02dd\b?\u0001"+
		"?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001"+
		"?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0003"+
		"?\u02f3\b?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001"+
		"?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001"+
		"?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001"+
		"?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001"+
		"?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001"+
		"?\u0001?\u0001?\u0001?\u0003?\u0329\b?\u0001?\u0001?\u0001?\u0005?\u032e"+
		"\b?\n?\f?\u0331\t?\u0001@\u0001@\u0001@\u0001@\u0003@\u0337\b@\u0001A"+
		"\u0001A\u0003A\u033b\bA\u0001A\u0001A\u0005A\u033f\bA\nA\fA\u0342\tA\u0001"+
		"A\u0003A\u0345\bA\u0001A\u0001A\u0003A\u0349\bA\u0001B\u0001B\u0001B\u0001"+
		"B\u0001C\u0003C\u0350\bC\u0001C\u0001C\u0001C\u0003C\u0355\bC\u0005C\u0357"+
		"\bC\nC\fC\u035a\tC\u0001D\u0001D\u0001D\u0005D\u035f\bD\nD\fD\u0362\t"+
		"D\u0001D\u0001D\u0001E\u0001E\u0001E\u0001E\u0001F\u0001F\u0001F\u0001"+
		"F\u0001F\u0001F\u0001F\u0003F\u0371\bF\u0001G\u0001G\u0001G\u0001G\u0001"+
		"G\u0001G\u0001G\u0001G\u0001G\u0001G\u0001G\u0001G\u0005G\u037f\bG\nG"+
		"\fG\u0382\tG\u0001G\u0003G\u0385\bG\u0001H\u0001H\u0001H\u0005H\u038a"+
		"\bH\nH\fH\u038d\tH\u0001H\u0000\u0001~I\u0000\u0002\u0004\u0006\b\n\f"+
		"\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:"+
		"<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a"+
		"\u008c\u008e\u0090\u0000\u0015\n\u0000AAJJTUYYaastvy}~\u0086\u0086\u0091"+
		"\u0091\u0001\u0000A\u0098\u000b\u0000KLRRVXZ[``hhllqqss\u0081\u0082\u0091"+
		"\u0092\u0005\u0000EFddmmrr\u008e\u008e\u0003\u0000MM``ss\u0002\u0000\u0083"+
		"\u0083\u0093\u0093\u0002\u0000DD\u0089\u0089\u0003\u0000PP^^gg\u0006\u0000"+
		"__ccno\u0081\u0082\u0089\u008a\u008d\u008d\u0001\u0000\u007f\u0080\u0003"+
		"\u0000\u0005\u0005\t\n\r1\u0003\u0000II{|\u008b\u008b\u0002\u0000\u0017"+
		"\u0018#$\u0001\u0000\u000e\u000f\u0003\u0000\u0013\u0013\u0016\u0016\u001b"+
		"\u001b\u0001\u0000\u0017\u0018\u0002\u0000\u001e\u001f11\u0002\u0000\t"+
		"\n!\"\u0002\u0000  --\u0004\u0000\u0005\u0005&)//28\u0001\u0000#$\u03de"+
		"\u0000\u0092\u0001\u0000\u0000\u0000\u0002\u009e\u0001\u0000\u0000\u0000"+
		"\u0004\u00c5\u0001\u0000\u0000\u0000\u0006\u00c7\u0001\u0000\u0000\u0000"+
		"\b\u00c9\u0001\u0000\u0000\u0000\n\u00ce\u0001\u0000\u0000\u0000\f\u00d6"+
		"\u0001\u0000\u0000\u0000\u000e\u00da\u0001\u0000\u0000\u0000\u0010\u00e8"+
		"\u0001\u0000\u0000\u0000\u0012\u00ea\u0001\u0000\u0000\u0000\u0014\u00ed"+
		"\u0001\u0000\u0000\u0000\u0016\u00f0\u0001\u0000\u0000\u0000\u0018\u0109"+
		"\u0001\u0000\u0000\u0000\u001a\u010d\u0001\u0000\u0000\u0000\u001c\u010f"+
		"\u0001\u0000\u0000\u0000\u001e\u011c\u0001\u0000\u0000\u0000 \u011e\u0001"+
		"\u0000\u0000\u0000\"\u0120\u0001\u0000\u0000\u0000$\u0122\u0001\u0000"+
		"\u0000\u0000&\u0129\u0001\u0000\u0000\u0000(\u0138\u0001\u0000\u0000\u0000"+
		"*\u013f\u0001\u0000\u0000\u0000,\u0145\u0001\u0000\u0000\u0000.\u0150"+
		"\u0001\u0000\u0000\u00000\u0160\u0001\u0000\u0000\u00002\u0167\u0001\u0000"+
		"\u0000\u00004\u016a\u0001\u0000\u0000\u00006\u0174\u0001\u0000\u0000\u0000"+
		"8\u0185\u0001\u0000\u0000\u0000:\u018c\u0001\u0000\u0000\u0000<\u019e"+
		"\u0001\u0000\u0000\u0000>\u01ab\u0001\u0000\u0000\u0000@\u01c0\u0001\u0000"+
		"\u0000\u0000B\u01c3\u0001\u0000\u0000\u0000D\u01c7\u0001\u0000\u0000\u0000"+
		"F\u01cc\u0001\u0000\u0000\u0000H\u01e9\u0001\u0000\u0000\u0000J\u01f2"+
		"\u0001\u0000\u0000\u0000L\u01f4\u0001\u0000\u0000\u0000N\u01f9\u0001\u0000"+
		"\u0000\u0000P\u0208\u0001\u0000\u0000\u0000R\u020a\u0001\u0000\u0000\u0000"+
		"T\u0216\u0001\u0000\u0000\u0000V\u021f\u0001\u0000\u0000\u0000X\u0221"+
		"\u0001\u0000\u0000\u0000Z\u0226\u0001\u0000\u0000\u0000\\\u0231\u0001"+
		"\u0000\u0000\u0000^\u0236\u0001\u0000\u0000\u0000`\u023f\u0001\u0000\u0000"+
		"\u0000b\u0256\u0001\u0000\u0000\u0000d\u0261\u0001\u0000\u0000\u0000f"+
		"\u026f\u0001\u0000\u0000\u0000h\u0271\u0001\u0000\u0000\u0000j\u0275\u0001"+
		"\u0000\u0000\u0000l\u027c\u0001\u0000\u0000\u0000n\u028d\u0001\u0000\u0000"+
		"\u0000p\u0291\u0001\u0000\u0000\u0000r\u0298\u0001\u0000\u0000\u0000t"+
		"\u02a1\u0001\u0000\u0000\u0000v\u02ae\u0001\u0000\u0000\u0000x\u02b4\u0001"+
		"\u0000\u0000\u0000z\u02c7\u0001\u0000\u0000\u0000|\u02c9\u0001\u0000\u0000"+
		"\u0000~\u02dc\u0001\u0000\u0000\u0000\u0080\u0336\u0001\u0000\u0000\u0000"+
		"\u0082\u0344\u0001\u0000\u0000\u0000\u0084\u034a\u0001\u0000\u0000\u0000"+
		"\u0086\u034f\u0001\u0000\u0000\u0000\u0088\u035b\u0001\u0000\u0000\u0000"+
		"\u008a\u0365\u0001\u0000\u0000\u0000\u008c\u0369\u0001\u0000\u0000\u0000"+
		"\u008e\u0384\u0001\u0000\u0000\u0000\u0090\u0386\u0001\u0000\u0000\u0000"+
		"\u0092\u0098\u0003\u0002\u0001\u0000\u0093\u0097\u0003\f\u0006\u0000\u0094"+
		"\u0097\u00034\u001a\u0000\u0095\u0097\u00038\u001c\u0000\u0096\u0093\u0001"+
		"\u0000\u0000\u0000\u0096\u0094\u0001\u0000\u0000\u0000\u0096\u0095\u0001"+
		"\u0000\u0000\u0000\u0097\u009a\u0001\u0000\u0000\u0000\u0098\u0096\u0001"+
		"\u0000\u0000\u0000\u0098\u0099\u0001\u0000\u0000\u0000\u0099\u009c\u0001"+
		"\u0000\u0000\u0000\u009a\u0098\u0001\u0000\u0000\u0000\u009b\u009d\u0003"+
		"\u0088D\u0000\u009c\u009b\u0001\u0000\u0000\u0000\u009c\u009d\u0001\u0000"+
		"\u0000\u0000\u009d\u0001\u0001\u0000\u0000\u0000\u009e\u009f\u0005H\u0000"+
		"\u0000\u009f\u00a2\u0003\b\u0004\u0000\u00a0\u00a1\u0005b\u0000\u0000"+
		"\u00a1\u00a3\u0003\n\u0005\u0000\u00a2\u00a0\u0001\u0000\u0000\u0000\u00a2"+
		"\u00a3\u0001\u0000\u0000\u0000\u00a3\u00a7\u0001\u0000\u0000\u0000\u00a4"+
		"\u00a6\u0003\u0004\u0002\u0000\u00a5\u00a4\u0001\u0000\u0000\u0000\u00a6"+
		"\u00a9\u0001\u0000\u0000\u0000\u00a7\u00a5\u0001\u0000\u0000\u0000\u00a7"+
		"\u00a8\u0001\u0000\u0000\u0000\u00a8\u00aa\u0001\u0000\u0000\u0000\u00a9"+
		"\u00a7\u0001\u0000\u0000\u0000\u00aa\u00ab\u0005\u0001\u0000\u0000\u00ab"+
		"\u0003\u0001\u0000\u0000\u0000\u00ac\u00c6\u0003\u0006\u0003\u0000\u00ad"+
		"\u00ae\u0005\u0097\u0000\u0000\u00ae\u00c6\u0003\n\u0005\u0000\u00af\u00b0"+
		"\u0005Q\u0000\u0000\u00b0\u00b1\u0005\u0002\u0000\u0000\u00b1\u00b2\u0003"+
		"\n\u0005\u0000\u00b2\u00b3\u0005\u0003\u0000\u0000\u00b3\u00c6\u0001\u0000"+
		"\u0000\u0000\u00b4\u00b9\u0005K\u0000\u0000\u00b5\u00b6\u0005\u0002\u0000"+
		"\u0000\u00b6\u00b7\u0003\n\u0005\u0000\u00b7\u00b8\u0005\u0003\u0000\u0000"+
		"\u00b8\u00ba\u0001\u0000\u0000\u0000\u00b9\u00b5\u0001\u0000\u0000\u0000"+
		"\u00b9\u00ba\u0001\u0000\u0000\u0000\u00ba\u00c6\u0001\u0000\u0000\u0000"+
		"\u00bb\u00bc\u0005i\u0000\u0000\u00bc\u00bd\u0005\u0002\u0000\u0000\u00bd"+
		"\u00be\u0003\u0090H\u0000\u00be\u00bf\u0005\u0003\u0000\u0000\u00bf\u00c6"+
		"\u0001\u0000\u0000\u0000\u00c0\u00c1\u0005\u0088\u0000\u0000\u00c1\u00c2"+
		"\u0005\u0002\u0000\u0000\u00c2\u00c3\u0003\u0090H\u0000\u00c3\u00c4\u0005"+
		"\u0003\u0000\u0000\u00c4\u00c6\u0001\u0000\u0000\u0000\u00c5\u00ac\u0001"+
		"\u0000\u0000\u0000\u00c5\u00ad\u0001\u0000\u0000\u0000\u00c5\u00af\u0001"+
		"\u0000\u0000\u0000\u00c5\u00b4\u0001\u0000\u0000\u0000\u00c5\u00bb\u0001"+
		"\u0000\u0000\u0000\u00c5\u00c0\u0001\u0000\u0000\u0000\u00c6\u0005\u0001"+
		"\u0000\u0000\u0000\u00c7\u00c8\u0007\u0000\u0000\u0000\u00c8\u0007\u0001"+
		"\u0000\u0000\u0000\u00c9\u00ca\u0007\u0001\u0000\u0000\u00ca\t\u0001\u0000"+
		"\u0000\u0000\u00cb\u00cc\u0003\b\u0004\u0000\u00cc\u00cd\u0005\u0004\u0000"+
		"\u0000\u00cd\u00cf\u0001\u0000\u0000\u0000\u00ce\u00cb\u0001\u0000\u0000"+
		"\u0000\u00ce\u00cf\u0001\u0000\u0000\u0000\u00cf\u00d0\u0001\u0000\u0000"+
		"\u0000\u00d0\u00d1\u0003\b\u0004\u0000\u00d1\u000b\u0001\u0000\u0000\u0000"+
		"\u00d2\u00d7\u0003\u000e\u0007\u0000\u00d3\u00d7\u0003\u0016\u000b\u0000"+
		"\u00d4\u00d7\u0003*\u0015\u0000\u00d5\u00d7\u0003.\u0017\u0000\u00d6\u00d2"+
		"\u0001\u0000\u0000\u0000\u00d6\u00d3\u0001\u0000\u0000\u0000\u00d6\u00d4"+
		"\u0001\u0000\u0000\u0000\u00d6\u00d5\u0001\u0000\u0000\u0000\u00d7\u00d8"+
		"\u0001\u0000\u0000\u0000\u00d8\u00d9\u0005\u0001\u0000\u0000\u00d9\r\u0001"+
		"\u0000\u0000\u0000\u00da\u00db\u0005L\u0000\u0000\u00db\u00dc\u0003\b"+
		"\u0004\u0000\u00dc\u00dd\u0005\u0005\u0000\u0000\u00dd\u00de\u0003~?\u0000"+
		"\u00de\u000f\u0001\u0000\u0000\u0000\u00df\u00e9\u0005:\u0000\u0000\u00e0"+
		"\u00e9\u0005;\u0000\u0000\u00e1\u00e9\u0005<\u0000\u0000\u00e2\u00e9\u0005"+
		"=\u0000\u0000\u00e3\u00e9\u0005>\u0000\u0000\u00e4\u00e9\u0005?\u0000"+
		"\u0000\u00e5\u00e9\u0003\u0012\t\u0000\u00e6\u00e9\u0003\u0014\n\u0000"+
		"\u00e7\u00e9\u0005@\u0000\u0000\u00e8\u00df\u0001\u0000\u0000\u0000\u00e8"+
		"\u00e0\u0001\u0000\u0000\u0000\u00e8\u00e1\u0001\u0000\u0000\u0000\u00e8"+
		"\u00e2\u0001\u0000\u0000\u0000\u00e8\u00e3\u0001\u0000\u0000\u0000\u00e8"+
		"\u00e4\u0001\u0000\u0000\u0000\u00e8\u00e5\u0001\u0000\u0000\u0000\u00e8"+
		"\u00e6\u0001\u0000\u0000\u0000\u00e8\u00e7\u0001\u0000\u0000\u0000\u00e9"+
		"\u0011\u0001\u0000\u0000\u0000\u00ea\u00eb\u0005H\u0000\u0000\u00eb\u00ec"+
		"\u0005;\u0000\u0000\u00ec\u0013\u0001\u0000\u0000\u0000\u00ed\u00ee\u0003"+
		"\b\u0004\u0000\u00ee\u00ef\u0005;\u0000\u0000\u00ef\u0015\u0001\u0000"+
		"\u0000\u0000\u00f0\u00f2\u0005\u0095\u0000\u0000\u00f1\u00f3\u0003\u001c"+
		"\u000e\u0000\u00f2\u00f1\u0001\u0000\u0000\u0000\u00f2\u00f3\u0001\u0000"+
		"\u0000\u0000\u00f3\u00f7\u0001\u0000\u0000\u0000\u00f4\u00f6\u0003\u001a"+
		"\r\u0000\u00f5\u00f4\u0001\u0000\u0000\u0000\u00f6\u00f9\u0001\u0000\u0000"+
		"\u0000\u00f7\u00f5\u0001\u0000\u0000\u0000\u00f7\u00f8\u0001\u0000\u0000"+
		"\u0000\u00f8\u00fa\u0001\u0000\u0000\u0000\u00f9\u00f7\u0001\u0000\u0000"+
		"\u0000\u00fa\u00fb\u0003\u001e\u000f\u0000\u00fb\u00fd\u0003\"\u0011\u0000"+
		"\u00fc\u00fe\u0003\u0018\f\u0000\u00fd\u00fc\u0001\u0000\u0000\u0000\u00fd"+
		"\u00fe\u0001\u0000\u0000\u0000\u00fe\u0106\u0001\u0000\u0000\u0000\u00ff"+
		"\u0100\u0005\u0006\u0000\u0000\u0100\u0102\u0003\"\u0011\u0000\u0101\u0103"+
		"\u0003\u0018\f\u0000\u0102\u0101\u0001\u0000\u0000\u0000\u0102\u0103\u0001"+
		"\u0000\u0000\u0000\u0103\u0105\u0001\u0000\u0000\u0000\u0104\u00ff\u0001"+
		"\u0000\u0000\u0000\u0105\u0108\u0001\u0000\u0000\u0000\u0106\u0104\u0001"+
		"\u0000\u0000\u0000\u0106\u0107\u0001\u0000\u0000\u0000\u0107\u0017\u0001"+
		"\u0000\u0000\u0000\u0108\u0106\u0001\u0000\u0000\u0000\u0109\u010a\u0005"+
		"\u0007\u0000\u0000\u010a\u010b\u0003~?\u0000\u010b\u010c\u0005\b\u0000"+
		"\u0000\u010c\u0019\u0001\u0000\u0000\u0000\u010d\u010e\u0007\u0002\u0000"+
		"\u0000\u010e\u001b\u0001\u0000\u0000\u0000\u010f\u0111\u0005\u0002\u0000"+
		"\u0000\u0110\u0112\u0003\b\u0004\u0000\u0111\u0110\u0001\u0000\u0000\u0000"+
		"\u0111\u0112\u0001\u0000\u0000\u0000\u0112\u0113\u0001\u0000\u0000\u0000"+
		"\u0113\u0114\u0005\u0003\u0000\u0000\u0114\u001d\u0001\u0000\u0000\u0000"+
		"\u0115\u011d\u0003$\u0012\u0000\u0116\u011d\u0003&\u0013\u0000\u0117\u011d"+
		"\u0003\n\u0005\u0000\u0118\u011d\u0003*\u0015\u0000\u0119\u011d\u0003"+
		".\u0017\u0000\u011a\u011d\u0003(\u0014\u0000\u011b\u011d\u0003 \u0010"+
		"\u0000\u011c\u0115\u0001\u0000\u0000\u0000\u011c\u0116\u0001\u0000\u0000"+
		"\u0000\u011c\u0117\u0001\u0000\u0000\u0000\u011c\u0118\u0001\u0000\u0000"+
		"\u0000\u011c\u0119\u0001\u0000\u0000\u0000\u011c\u011a\u0001\u0000\u0000"+
		"\u0000\u011c\u011b\u0001\u0000\u0000\u0000\u011d\u001f\u0001\u0000\u0000"+
		"\u0000\u011e\u011f\u0007\u0003\u0000\u0000\u011f!\u0001\u0000\u0000\u0000"+
		"\u0120\u0121\u0003\b\u0004\u0000\u0121#\u0001\u0000\u0000\u0000\u0122"+
		"\u0123\u0003\b\u0004\u0000\u0123\u0125\u0005\u0007\u0000\u0000\u0124\u0126"+
		"\u0003~?\u0000\u0125\u0124\u0001\u0000\u0000\u0000\u0125\u0126\u0001\u0000"+
		"\u0000\u0000\u0126\u0127\u0001\u0000\u0000\u0000\u0127\u0128\u0005\b\u0000"+
		"\u0000\u0128%\u0001\u0000\u0000\u0000\u0129\u012a\u0005B\u0000\u0000\u012a"+
		"\u012e\u0005\t\u0000\u0000\u012b\u012d\u0003\u001a\r\u0000\u012c\u012b"+
		"\u0001\u0000\u0000\u0000\u012d\u0130\u0001\u0000\u0000\u0000\u012e\u012c"+
		"\u0001\u0000\u0000\u0000\u012e\u012f\u0001\u0000\u0000\u0000\u012f\u0134"+
		"\u0001\u0000\u0000\u0000\u0130\u012e\u0001\u0000\u0000\u0000\u0131\u0135"+
		"\u0003\n\u0005\u0000\u0132\u0135\u0003(\u0014\u0000\u0133\u0135\u0003"+
		" \u0010\u0000\u0134\u0131\u0001\u0000\u0000\u0000\u0134\u0132\u0001\u0000"+
		"\u0000\u0000\u0134\u0133\u0001\u0000\u0000\u0000\u0135\u0136\u0001\u0000"+
		"\u0000\u0000\u0136\u0137\u0005\n\u0000\u0000\u0137\'\u0001\u0000\u0000"+
		"\u0000\u0138\u013d\u0005H\u0000\u0000\u0139\u013a\u0005\t\u0000\u0000"+
		"\u013a\u013b\u0003\n\u0005\u0000\u013b\u013c\u0005\n\u0000\u0000\u013c"+
		"\u013e\u0001\u0000\u0000\u0000\u013d\u0139\u0001\u0000\u0000\u0000\u013d"+
		"\u013e\u0001\u0000\u0000\u0000\u013e)\u0001\u0000\u0000\u0000\u013f\u0140"+
		"\u0005]\u0000\u0000\u0140\u0141\u0003\b\u0004\u0000\u0141\u0142\u0005"+
		"\u000b\u0000\u0000\u0142\u0143\u0003,\u0016\u0000\u0143\u0144\u0005\f"+
		"\u0000\u0000\u0144+\u0001\u0000\u0000\u0000\u0145\u014a\u0003\b\u0004"+
		"\u0000\u0146\u0147\u0005\u0006\u0000\u0000\u0147\u0149\u0003\b\u0004\u0000"+
		"\u0148\u0146\u0001\u0000\u0000\u0000\u0149\u014c\u0001\u0000\u0000\u0000"+
		"\u014a\u0148\u0001\u0000\u0000\u0000\u014a\u014b\u0001\u0000\u0000\u0000"+
		"\u014b\u014e\u0001\u0000\u0000\u0000\u014c\u014a\u0001\u0000\u0000\u0000"+
		"\u014d\u014f\u0005\u0006\u0000\u0000\u014e\u014d\u0001\u0000\u0000\u0000"+
		"\u014e\u014f\u0001\u0000\u0000\u0000\u014f-\u0001\u0000\u0000\u0000\u0150"+
		"\u0154\u0005\u008f\u0000\u0000\u0151\u0153\u00030\u0018\u0000\u0152\u0151"+
		"\u0001\u0000\u0000\u0000\u0153\u0156\u0001\u0000\u0000\u0000\u0154\u0152"+
		"\u0001\u0000\u0000\u0000\u0154\u0155\u0001\u0000\u0000\u0000\u0155\u0157"+
		"\u0001\u0000\u0000\u0000\u0156\u0154\u0001\u0000\u0000\u0000\u0157\u015a"+
		"\u0003\b\u0004\u0000\u0158\u0159\u0005b\u0000\u0000\u0159\u015b\u0003"+
		"\n\u0005\u0000\u015a\u0158\u0001\u0000\u0000\u0000\u015a\u015b\u0001\u0000"+
		"\u0000\u0000\u015b\u015c\u0001\u0000\u0000\u0000\u015c\u015d\u0005\u000b"+
		"\u0000\u0000\u015d\u015e\u00032\u0019\u0000\u015e\u015f\u0005\f\u0000"+
		"\u0000\u015f/\u0001\u0000\u0000\u0000\u0160\u0161\u0007\u0004\u0000\u0000"+
		"\u01611\u0001\u0000\u0000\u0000\u0162\u0163\u0003\u0016\u000b\u0000\u0163"+
		"\u0164\u0005\u0001\u0000\u0000\u0164\u0166\u0001\u0000\u0000\u0000\u0165"+
		"\u0162\u0001\u0000\u0000\u0000\u0166\u0169\u0001\u0000\u0000\u0000\u0167"+
		"\u0165\u0001\u0000\u0000\u0000\u0167\u0168\u0001\u0000\u0000\u0000\u0168"+
		"3\u0001\u0000\u0000\u0000\u0169\u0167\u0001\u0000\u0000\u0000\u016a\u016b"+
		"\u0005\u0084\u0000\u0000\u016b\u016f\u0005\u000b\u0000\u0000\u016c\u016e"+
		"\u00036\u001b\u0000\u016d\u016c\u0001\u0000\u0000\u0000\u016e\u0171\u0001"+
		"\u0000\u0000\u0000\u016f\u016d\u0001\u0000\u0000\u0000\u016f\u0170\u0001"+
		"\u0000\u0000\u0000\u0170\u0172\u0001\u0000\u0000\u0000\u0171\u016f\u0001"+
		"\u0000\u0000\u0000\u0172\u0173\u0005\f\u0000\u0000\u01735\u0001\u0000"+
		"\u0000\u0000\u0174\u0175\u0007\u0005\u0000\u0000\u0175\u0176\u0005j\u0000"+
		"\u0000\u0176\u0177\u0005\u0002\u0000\u0000\u0177\u0178\u0003~?\u0000\u0178"+
		"\u0179\u0005\u0003\u0000\u0000\u0179\u017e\u0003\b\u0004\u0000\u017a\u017b"+
		"\u0005\u0006\u0000\u0000\u017b\u017d\u0003\b\u0004\u0000\u017c\u017a\u0001"+
		"\u0000\u0000\u0000\u017d\u0180\u0001\u0000\u0000\u0000\u017e\u017c\u0001"+
		"\u0000\u0000\u0000\u017e\u017f\u0001\u0000\u0000\u0000\u017f\u0181\u0001"+
		"\u0000\u0000\u0000\u0180\u017e\u0001\u0000\u0000\u0000\u0181\u0182\u0005"+
		"\u0001\u0000\u0000\u01827\u0001\u0000\u0000\u0000\u0183\u0186\u0003:\u001d"+
		"\u0000\u0184\u0186\u0003D\"\u0000\u0185\u0183\u0001\u0000\u0000\u0000"+
		"\u0185\u0184\u0001\u0000\u0000\u0000\u0186\u0187\u0001\u0000\u0000\u0000"+
		"\u0187\u0185\u0001\u0000\u0000\u0000\u0187\u0188\u0001\u0000\u0000\u0000"+
		"\u01889\u0001\u0000\u0000\u0000\u0189\u018b\u0003B!\u0000\u018a\u0189"+
		"\u0001\u0000\u0000\u0000\u018b\u018e\u0001\u0000\u0000\u0000\u018c\u018a"+
		"\u0001\u0000\u0000\u0000\u018c\u018d\u0001\u0000\u0000\u0000\u018d\u018f"+
		"\u0001\u0000\u0000\u0000\u018e\u018c\u0001\u0000\u0000\u0000\u018f\u0192"+
		"\u0005\u008c\u0000\u0000\u0190\u0191\u0005\u0002\u0000\u0000\u0191\u0193"+
		"\u0005\u0003\u0000\u0000\u0192\u0190\u0001\u0000\u0000\u0000\u0192\u0193"+
		"\u0001\u0000\u0000\u0000\u0193\u0194\u0001\u0000\u0000\u0000\u0194\u0196"+
		"\u0003\b\u0004\u0000\u0195\u0197\u0003\u001c\u000e\u0000\u0196\u0195\u0001"+
		"\u0000\u0000\u0000\u0196\u0197\u0001\u0000\u0000\u0000\u0197\u019a\u0001"+
		"\u0000\u0000\u0000\u0198\u0199\u0005b\u0000\u0000\u0199\u019b\u0003\b"+
		"\u0004\u0000\u019a\u0198\u0001\u0000\u0000\u0000\u019a\u019b\u0001\u0000"+
		"\u0000\u0000\u019b\u019c\u0001\u0000\u0000\u0000\u019c\u019d\u0003<\u001e"+
		"\u0000\u019d;\u0001\u0000\u0000\u0000\u019e\u01a0\u0005\u000b\u0000\u0000"+
		"\u019f\u01a1\u0003>\u001f\u0000\u01a0\u019f\u0001\u0000\u0000\u0000\u01a0"+
		"\u01a1\u0001\u0000\u0000\u0000\u01a1\u01a5\u0001\u0000\u0000\u0000\u01a2"+
		"\u01a4\u0003D\"\u0000\u01a3\u01a2\u0001\u0000\u0000\u0000\u01a4\u01a7"+
		"\u0001\u0000\u0000\u0000\u01a5\u01a3\u0001\u0000\u0000\u0000\u01a5\u01a6"+
		"\u0001\u0000\u0000\u0000\u01a6\u01a8\u0001\u0000\u0000\u0000\u01a7\u01a5"+
		"\u0001\u0000\u0000\u0000\u01a8\u01a9\u0003@ \u0000\u01a9\u01aa\u0005\f"+
		"\u0000\u0000\u01aa=\u0001\u0000\u0000\u0000\u01ab\u01ac\u0005k\u0000\u0000"+
		"\u01ac\u01b1\u0003\b\u0004\u0000\u01ad\u01ae\u0005\u0006\u0000\u0000\u01ae"+
		"\u01b0\u0003\b\u0004\u0000\u01af\u01ad\u0001\u0000\u0000\u0000\u01b0\u01b3"+
		"\u0001\u0000\u0000\u0000\u01b1\u01af\u0001\u0000\u0000\u0000\u01b1\u01b2"+
		"\u0001\u0000\u0000\u0000\u01b2\u01b4\u0001\u0000\u0000\u0000\u01b3\u01b1"+
		"\u0001\u0000\u0000\u0000\u01b4\u01b5\u0005\u0001\u0000\u0000\u01b5?\u0001"+
		"\u0000\u0000\u0000\u01b6\u01b7\u0003\b\u0004\u0000\u01b7\u01bb\u0005\r"+
		"\u0000\u0000\u01b8\u01ba\u0003f3\u0000\u01b9\u01b8\u0001\u0000\u0000\u0000"+
		"\u01ba\u01bd\u0001\u0000\u0000\u0000\u01bb\u01b9\u0001\u0000\u0000\u0000"+
		"\u01bb\u01bc\u0001\u0000\u0000\u0000\u01bc\u01bf\u0001\u0000\u0000\u0000"+
		"\u01bd\u01bb\u0001\u0000\u0000\u0000\u01be\u01b6\u0001\u0000\u0000\u0000"+
		"\u01bf\u01c2\u0001\u0000\u0000\u0000\u01c0\u01be\u0001\u0000\u0000\u0000"+
		"\u01c0\u01c1\u0001\u0000\u0000\u0000\u01c1A\u0001\u0000\u0000\u0000\u01c2"+
		"\u01c0\u0001\u0000\u0000\u0000\u01c3\u01c4\u0007\u0006\u0000\u0000\u01c4"+
		"C\u0001\u0000\u0000\u0000\u01c5\u01c8\u0003F#\u0000\u01c6\u01c8\u0003"+
		"N\'\u0000\u01c7\u01c5\u0001\u0000\u0000\u0000\u01c7\u01c6\u0001\u0000"+
		"\u0000\u0000\u01c8E\u0001\u0000\u0000\u0000\u01c9\u01cb\u0003J%\u0000"+
		"\u01ca\u01c9\u0001\u0000\u0000\u0000\u01cb\u01ce\u0001\u0000\u0000\u0000"+
		"\u01cc\u01ca\u0001\u0000\u0000\u0000\u01cc\u01cd\u0001\u0000\u0000\u0000"+
		"\u01cd\u01cf\u0001\u0000\u0000\u0000\u01ce\u01cc\u0001\u0000\u0000\u0000"+
		"\u01cf\u01d1\u0003H$\u0000\u01d0\u01d2\u0003b1\u0000\u01d1\u01d0\u0001"+
		"\u0000\u0000\u0000\u01d1\u01d2\u0001\u0000\u0000\u0000\u01d2\u01d3\u0001"+
		"\u0000\u0000\u0000\u01d3\u01d4\u0003\b\u0004\u0000\u01d4\u01dd\u0005\u0002"+
		"\u0000\u0000\u01d5\u01da\u0003Z-\u0000\u01d6\u01d7\u0005\u0006\u0000\u0000"+
		"\u01d7\u01d9\u0003Z-\u0000\u01d8\u01d6\u0001\u0000\u0000\u0000\u01d9\u01dc"+
		"\u0001\u0000\u0000\u0000\u01da\u01d8\u0001\u0000\u0000\u0000\u01da\u01db"+
		"\u0001\u0000\u0000\u0000\u01db\u01de\u0001\u0000\u0000\u0000\u01dc\u01da"+
		"\u0001\u0000\u0000\u0000\u01dd\u01d5\u0001\u0000\u0000\u0000\u01dd\u01de"+
		"\u0001\u0000\u0000\u0000\u01de\u01df\u0001\u0000\u0000\u0000\u01df\u01e4"+
		"\u0005\u0003\u0000\u0000\u01e0\u01e1\u0005\u000b\u0000\u0000\u01e1\u01e2"+
		"\u0003^/\u0000\u01e2\u01e3\u0005\f\u0000\u0000\u01e3\u01e5\u0001\u0000"+
		"\u0000\u0000\u01e4\u01e0\u0001\u0000\u0000\u0000\u01e4\u01e5\u0001\u0000"+
		"\u0000\u0000\u01e5\u01e7\u0001\u0000\u0000\u0000\u01e6\u01e8\u0005\u0001"+
		"\u0000\u0000\u01e7\u01e6\u0001\u0000\u0000\u0000\u01e7\u01e8\u0001\u0000"+
		"\u0000\u0000\u01e8G\u0001\u0000\u0000\u0000\u01e9\u01ea\u0007\u0007\u0000"+
		"\u0000\u01eaI\u0001\u0000\u0000\u0000\u01eb\u01f3\u0003L&\u0000\u01ec"+
		"\u01f0\u0005s\u0000\u0000\u01ed\u01ee\u0005\u0002\u0000\u0000\u01ee\u01ef"+
		"\u0005<\u0000\u0000\u01ef\u01f1\u0005\u0003\u0000\u0000\u01f0\u01ed\u0001"+
		"\u0000\u0000\u0000\u01f0\u01f1\u0001\u0000\u0000\u0000\u01f1\u01f3\u0001"+
		"\u0000\u0000\u0000\u01f2\u01eb\u0001\u0000\u0000\u0000\u01f2\u01ec\u0001"+
		"\u0000\u0000\u0000\u01f3K\u0001\u0000\u0000\u0000\u01f4\u01f5\u0007\b"+
		"\u0000\u0000\u01f5M\u0001\u0000\u0000\u0000\u01f6\u01f8\u0003J%\u0000"+
		"\u01f7\u01f6\u0001\u0000\u0000\u0000\u01f8\u01fb\u0001\u0000\u0000\u0000"+
		"\u01f9\u01f7\u0001\u0000\u0000\u0000\u01f9\u01fa\u0001\u0000\u0000\u0000"+
		"\u01fa\u01fc\u0001\u0000\u0000\u0000\u01fb\u01f9\u0001\u0000\u0000\u0000"+
		"\u01fc\u0201\u0003P(\u0000\u01fd\u01fe\u0005\u000b\u0000\u0000\u01fe\u01ff"+
		"\u0003^/\u0000\u01ff\u0200\u0005\f\u0000\u0000\u0200\u0202\u0001\u0000"+
		"\u0000\u0000\u0201\u01fd\u0001\u0000\u0000\u0000\u0201\u0202\u0001\u0000"+
		"\u0000\u0000\u0202\u0204\u0001\u0000\u0000\u0000\u0203\u0205\u0005\u0001"+
		"\u0000\u0000\u0204\u0203\u0001\u0000\u0000\u0000\u0204\u0205\u0001\u0000"+
		"\u0000\u0000\u0205O\u0001\u0000\u0000\u0000\u0206\u0209\u0003R)\u0000"+
		"\u0207\u0209\u0003T*\u0000\u0208\u0206\u0001\u0000\u0000\u0000\u0208\u0207"+
		"\u0001\u0000\u0000\u0000\u0209Q\u0001\u0000\u0000\u0000\u020a\u020b\u0005"+
		"z\u0000\u0000\u020b\u020c\u0005\u0002\u0000\u0000\u020c\u020d\u0005<\u0000"+
		"\u0000\u020d\u020e\u0005\u0003\u0000\u0000\u020e\u020f\u0003b1\u0000\u020f"+
		"\u0210\u0003V+\u0000\u0210\u0211\u0005\u0002\u0000\u0000\u0211\u0212\u0003"+
		"Z-\u0000\u0212\u0213\u0005\u0006\u0000\u0000\u0213\u0214\u0003Z-\u0000"+
		"\u0214\u0215\u0005\u0003\u0000\u0000\u0215S\u0001\u0000\u0000\u0000\u0216"+
		"\u0217\u0007\t\u0000\u0000\u0217\u0218\u0003b1\u0000\u0218\u0219\u0003"+
		"V+\u0000\u0219\u021a\u0005\u0002\u0000\u0000\u021a\u021b\u0003Z-\u0000"+
		"\u021b\u021c\u0005\u0003\u0000\u0000\u021cU\u0001\u0000\u0000\u0000\u021d"+
		"\u0220\u0003\b\u0004\u0000\u021e\u0220\u0003X,\u0000\u021f\u021d\u0001"+
		"\u0000\u0000\u0000\u021f\u021e\u0001\u0000\u0000\u0000\u0220W\u0001\u0000"+
		"\u0000\u0000\u0221\u0222\u0007\n\u0000\u0000\u0222Y\u0001\u0000\u0000"+
		"\u0000\u0223\u0225\u0007\u000b\u0000\u0000\u0224\u0223\u0001\u0000\u0000"+
		"\u0000\u0225\u0228\u0001\u0000\u0000\u0000\u0226\u0224\u0001\u0000\u0000"+
		"\u0000\u0226\u0227\u0001\u0000\u0000\u0000\u0227\u0229\u0001\u0000\u0000"+
		"\u0000\u0228\u0226\u0001\u0000\u0000\u0000\u0229\u022a\u0003\\.\u0000"+
		"\u022a\u022b\u0003\b\u0004\u0000\u022b[\u0001\u0000\u0000\u0000\u022c"+
		"\u0232\u0003$\u0012\u0000\u022d\u0232\u0003&\u0013\u0000\u022e\u0232\u0003"+
		"\n\u0005\u0000\u022f\u0232\u0003(\u0014\u0000\u0230\u0232\u0003 \u0010"+
		"\u0000\u0231\u022c\u0001\u0000\u0000\u0000\u0231\u022d\u0001\u0000\u0000"+
		"\u0000\u0231\u022e\u0001\u0000\u0000\u0000\u0231\u022f\u0001\u0000\u0000"+
		"\u0000\u0231\u0230\u0001\u0000\u0000\u0000\u0232]\u0001\u0000\u0000\u0000"+
		"\u0233\u0235\u0003`0\u0000\u0234\u0233\u0001\u0000\u0000\u0000\u0235\u0238"+
		"\u0001\u0000\u0000\u0000\u0236\u0234\u0001\u0000\u0000\u0000\u0236\u0237"+
		"\u0001\u0000\u0000\u0000\u0237\u023c\u0001\u0000\u0000\u0000\u0238\u0236"+
		"\u0001\u0000\u0000\u0000\u0239\u023b\u0003f3\u0000\u023a\u0239\u0001\u0000"+
		"\u0000\u0000\u023b\u023e\u0001\u0000\u0000\u0000\u023c\u023a\u0001\u0000"+
		"\u0000\u0000\u023c\u023d\u0001\u0000\u0000\u0000\u023d_\u0001\u0000\u0000"+
		"\u0000\u023e\u023c\u0001\u0000\u0000\u0000\u023f\u0240\u0005p\u0000\u0000"+
		"\u0240\u0241\u0003b1\u0000\u0241\u0243\u0003\b\u0004\u0000\u0242\u0244"+
		"\u0003\u0018\f\u0000\u0243\u0242\u0001\u0000\u0000\u0000\u0243\u0244\u0001"+
		"\u0000\u0000\u0000\u0244\u024c\u0001\u0000\u0000\u0000\u0245\u0246\u0005"+
		"\u0006\u0000\u0000\u0246\u0248\u0003\b\u0004\u0000\u0247\u0249\u0003\u0018"+
		"\f\u0000\u0248\u0247\u0001\u0000\u0000\u0000\u0248\u0249\u0001\u0000\u0000"+
		"\u0000\u0249\u024b\u0001\u0000\u0000\u0000\u024a\u0245\u0001\u0000\u0000"+
		"\u0000\u024b\u024e\u0001\u0000\u0000\u0000\u024c\u024a\u0001\u0000\u0000"+
		"\u0000\u024c\u024d\u0001\u0000\u0000\u0000\u024d\u024f\u0001\u0000\u0000"+
		"\u0000\u024e\u024c\u0001\u0000\u0000\u0000\u024f\u0250\u0005\u0001\u0000"+
		"\u0000\u0250a\u0001\u0000\u0000\u0000\u0251\u0257\u0003\n\u0005\u0000"+
		"\u0252\u0257\u0003$\u0012\u0000\u0253\u0257\u0003&\u0013\u0000\u0254\u0257"+
		"\u0003(\u0014\u0000\u0255\u0257\u0003 \u0010\u0000\u0256\u0251\u0001\u0000"+
		"\u0000\u0000\u0256\u0252\u0001\u0000\u0000\u0000\u0256\u0253\u0001\u0000"+
		"\u0000\u0000\u0256\u0254\u0001\u0000\u0000\u0000\u0256\u0255\u0001\u0000"+
		"\u0000\u0000\u0257c\u0001\u0000\u0000\u0000\u0258\u0262\u0003f3\u0000"+
		"\u0259\u025d\u0005\u000b\u0000\u0000\u025a\u025c\u0003f3\u0000\u025b\u025a"+
		"\u0001\u0000\u0000\u0000\u025c\u025f\u0001\u0000\u0000\u0000\u025d\u025b"+
		"\u0001\u0000\u0000\u0000\u025d\u025e\u0001\u0000\u0000\u0000\u025e\u0260"+
		"\u0001\u0000\u0000\u0000\u025f\u025d\u0001\u0000\u0000\u0000\u0260\u0262"+
		"\u0005\f\u0000\u0000\u0261\u0258\u0001\u0000\u0000\u0000\u0261\u0259\u0001"+
		"\u0000\u0000\u0000\u0262e\u0001\u0000\u0000\u0000\u0263\u0270\u0005\u0001"+
		"\u0000\u0000\u0264\u0270\u0003h4\u0000\u0265\u0270\u0003j5\u0000\u0266"+
		"\u0270\u0003l6\u0000\u0267\u0270\u0003n7\u0000\u0268\u0270\u0003p8\u0000"+
		"\u0269\u0270\u0003r9\u0000\u026a\u0270\u0003t:\u0000\u026b\u0270\u0003"+
		"v;\u0000\u026c\u026d\u0003~?\u0000\u026d\u026e\u0005\u0001\u0000\u0000"+
		"\u026e\u0270\u0001\u0000\u0000\u0000\u026f\u0263\u0001\u0000\u0000\u0000"+
		"\u026f\u0264\u0001\u0000\u0000\u0000\u026f\u0265\u0001\u0000\u0000\u0000"+
		"\u026f\u0266\u0001\u0000\u0000\u0000\u026f\u0267\u0001\u0000\u0000\u0000"+
		"\u026f\u0268\u0001\u0000\u0000\u0000\u026f\u0269\u0001\u0000\u0000\u0000"+
		"\u026f\u026a\u0001\u0000\u0000\u0000\u026f\u026b\u0001\u0000\u0000\u0000"+
		"\u026f\u026c\u0001\u0000\u0000\u0000\u0270g\u0001\u0000\u0000\u0000\u0271"+
		"\u0272\u0005C\u0000\u0000\u0272\u0273\u0003~?\u0000\u0273\u0274\u0005"+
		"\u0001\u0000\u0000\u0274i\u0001\u0000\u0000\u0000\u0275\u0276\u0005j\u0000"+
		"\u0000\u0276\u0277\u0003\u0084B\u0000\u0277\u027a\u0003d2\u0000\u0278"+
		"\u0279\u0005\\\u0000\u0000\u0279\u027b\u0003d2\u0000\u027a\u0278\u0001"+
		"\u0000\u0000\u0000\u027a\u027b\u0001\u0000\u0000\u0000\u027bk\u0001\u0000"+
		"\u0000\u0000\u027c\u027f\u0005\u0090\u0000\u0000\u027d\u0280\u0003\u0084"+
		"B\u0000\u027e\u0280\u0003~?\u0000\u027f\u027d\u0001\u0000\u0000\u0000"+
		"\u027f\u027e\u0001\u0000\u0000\u0000\u0280\u0281\u0001\u0000\u0000\u0000"+
		"\u0281\u0285\u0005\u000b\u0000\u0000\u0282\u0284\u0003x<\u0000\u0283\u0282"+
		"\u0001\u0000\u0000\u0000\u0284\u0287\u0001\u0000\u0000\u0000\u0285\u0283"+
		"\u0001\u0000\u0000\u0000\u0285\u0286\u0001\u0000\u0000\u0000\u0286\u0289"+
		"\u0001\u0000\u0000\u0000\u0287\u0285\u0001\u0000\u0000\u0000\u0288\u028a"+
		"\u0003|>\u0000\u0289\u0288\u0001\u0000\u0000\u0000\u0289\u028a\u0001\u0000"+
		"\u0000\u0000\u028a\u028b\u0001\u0000\u0000\u0000\u028b\u028c\u0005\f\u0000"+
		"\u0000\u028cm\u0001\u0000\u0000\u0000\u028d\u028e\u0005\u0096\u0000\u0000"+
		"\u028e\u028f\u0003\u0084B\u0000\u028f\u0290\u0003d2\u0000\u0290o\u0001"+
		"\u0000\u0000\u0000\u0291\u0292\u0005S\u0000\u0000\u0292\u0293\u0003d2"+
		"\u0000\u0293\u0294\u0005\u0094\u0000\u0000\u0294\u0295\u0005\u0002\u0000"+
		"\u0000\u0295\u0296\u0003~?\u0000\u0296\u0297\u0005\u0003\u0000\u0000\u0297"+
		"q\u0001\u0000\u0000\u0000\u0298\u0299\u0005f\u0000\u0000\u0299\u029a\u0003"+
		"\u008eG\u0000\u029a\u029c\u0005\u0002\u0000\u0000\u029b\u029d\u0003\u0086"+
		"C\u0000\u029c\u029b\u0001\u0000\u0000\u0000\u029c\u029d\u0001\u0000\u0000"+
		"\u0000\u029d\u029e\u0001\u0000\u0000\u0000\u029e\u029f\u0005\u0003\u0000"+
		"\u0000\u029f\u02a0\u0003d2\u0000\u02a0s\u0001\u0000\u0000\u0000\u02a1"+
		"\u02a2\u0005e\u0000\u0000\u02a2\u02a3\u0005\u0002\u0000\u0000\u02a3\u02a4"+
		"\u0003\b\u0004\u0000\u02a4\u02a5\u0005\u0005\u0000\u0000\u02a5\u02a6\u0003"+
		"~?\u0000\u02a6\u02a7\u0005\u0001\u0000\u0000\u02a7\u02a8\u0003~?\u0000"+
		"\u02a8\u02a9\u0005\u0001\u0000\u0000\u02a9\u02aa\u0003~?\u0000\u02aa\u02ac"+
		"\u0005\u0003\u0000\u0000\u02ab\u02ad\u0003d2\u0000\u02ac\u02ab\u0001\u0000"+
		"\u0000\u0000\u02ac\u02ad\u0001\u0000\u0000\u0000\u02adu\u0001\u0000\u0000"+
		"\u0000\u02ae\u02b0\u0005\u0085\u0000\u0000\u02af\u02b1\u0003~?\u0000\u02b0"+
		"\u02af\u0001\u0000\u0000\u0000\u02b0\u02b1\u0001\u0000\u0000\u0000\u02b1"+
		"\u02b2\u0001\u0000\u0000\u0000\u02b2\u02b3\u0005\u0001\u0000\u0000\u02b3"+
		"w\u0001\u0000\u0000\u0000\u02b4\u02b5\u0005G\u0000\u0000\u02b5\u02b6\u0003"+
		"~?\u0000\u02b6\u02b7\u0005\r\u0000\u0000\u02b7\u02b8\u0003z=\u0000\u02b8"+
		"y\u0001\u0000\u0000\u0000\u02b9\u02bb\u0003f3\u0000\u02ba\u02b9\u0001"+
		"\u0000\u0000\u0000\u02bb\u02be\u0001\u0000\u0000\u0000\u02bc\u02ba\u0001"+
		"\u0000\u0000\u0000\u02bc\u02bd\u0001\u0000\u0000\u0000\u02bd\u02c8\u0001"+
		"\u0000\u0000\u0000\u02be\u02bc\u0001\u0000\u0000\u0000\u02bf\u02c3\u0005"+
		"\u000b\u0000\u0000\u02c0\u02c2\u0003f3\u0000\u02c1\u02c0\u0001\u0000\u0000"+
		"\u0000\u02c2\u02c5\u0001\u0000\u0000\u0000\u02c3\u02c1\u0001\u0000\u0000"+
		"\u0000\u02c3\u02c4\u0001\u0000\u0000\u0000\u02c4\u02c6\u0001\u0000\u0000"+
		"\u0000\u02c5\u02c3\u0001\u0000\u0000\u0000\u02c6\u02c8\u0005\f\u0000\u0000"+
		"\u02c7\u02bc\u0001\u0000\u0000\u0000\u02c7\u02bf\u0001\u0000\u0000\u0000"+
		"\u02c8{\u0001\u0000\u0000\u0000\u02c9\u02ca\u0005N\u0000\u0000\u02ca\u02cb"+
		"\u0005\r\u0000\u0000\u02cb\u02cc\u0003z=\u0000\u02cc}\u0001\u0000\u0000"+
		"\u0000\u02cd\u02ce\u0006?\uffff\uffff\u0000\u02ce\u02dd\u0003\u0080@\u0000"+
		"\u02cf\u02d0\u0003 \u0010\u0000\u02d0\u02d2\u0005\u0002\u0000\u0000\u02d1"+
		"\u02d3\u0003\u0086C\u0000\u02d2\u02d1\u0001\u0000\u0000\u0000\u02d2\u02d3"+
		"\u0001\u0000\u0000\u0000\u02d3\u02d4\u0001\u0000\u0000\u0000\u02d4\u02d5"+
		"\u0005\u0003\u0000\u0000\u02d5\u02dd\u0001\u0000\u0000\u0000\u02d6\u02d7"+
		"\u0005u\u0000\u0000\u02d7\u02dd\u0003\u0082A\u0000\u02d8\u02d9\u0007\f"+
		"\u0000\u0000\u02d9\u02dd\u0003~?\u0013\u02da\u02db\u0007\r\u0000\u0000"+
		"\u02db\u02dd\u0003~?\u0012\u02dc\u02cd\u0001\u0000\u0000\u0000\u02dc\u02cf"+
		"\u0001\u0000\u0000\u0000\u02dc\u02d6\u0001\u0000\u0000\u0000\u02dc\u02d8"+
		"\u0001\u0000\u0000\u0000\u02dc\u02da\u0001\u0000\u0000\u0000\u02dd\u032f"+
		"\u0001\u0000\u0000\u0000\u02de\u02df\n\u0011\u0000\u0000\u02df\u02e0\u0007"+
		"\u000e\u0000\u0000\u02e0\u032e\u0003~?\u0012\u02e1\u02e2\n\u0010\u0000"+
		"\u0000\u02e2\u02e3\u0007\u000f\u0000\u0000\u02e3\u032e\u0003~?\u0011\u02e4"+
		"\u02e5\n\u000f\u0000\u0000\u02e5\u02e6\u0005,\u0000\u0000\u02e6\u032e"+
		"\u0003~?\u0010\u02e7\u02e8\n\u000e\u0000\u0000\u02e8\u02e9\u0007\u0010"+
		"\u0000\u0000\u02e9\u032e\u0003~?\u000f\u02ea\u02f2\n\r\u0000\u0000\u02eb"+
		"\u02ec\u0005\t\u0000\u0000\u02ec\u02f3\u0005\t\u0000\u0000\u02ed\u02ee"+
		"\u0005\n\u0000\u0000\u02ee\u02ef\u0005\n\u0000\u0000\u02ef\u02f3\u0005"+
		"\n\u0000\u0000\u02f0\u02f1\u0005\n\u0000\u0000\u02f1\u02f3\u0005\n\u0000"+
		"\u0000\u02f2\u02eb\u0001\u0000\u0000\u0000\u02f2\u02ed\u0001\u0000\u0000"+
		"\u0000\u02f2\u02f0\u0001\u0000\u0000\u0000\u02f3\u02f4\u0001\u0000\u0000"+
		"\u0000\u02f4\u032e\u0003~?\u000e\u02f5\u02f6\n\f\u0000\u0000\u02f6\u02f7"+
		"\u0007\u0011\u0000\u0000\u02f7\u032e\u0003~?\r\u02f8\u02f9\n\u000b\u0000"+
		"\u0000\u02f9\u02fa\u0007\u0012\u0000\u0000\u02fa\u032e\u0003~?\f\u02fb"+
		"\u02fc\n\n\u0000\u0000\u02fc\u02fd\u0003\b\u0004\u0000\u02fd\u02fe\u0003"+
		"~?\u000b\u02fe\u032e\u0001\u0000\u0000\u0000\u02ff\u0300\n\t\u0000\u0000"+
		"\u0300\u0301\u0005\u0010\u0000\u0000\u0301\u032e\u0003~?\n\u0302\u0303"+
		"\n\b\u0000\u0000\u0303\u0304\u0005\u0012\u0000\u0000\u0304\u032e\u0003"+
		"~?\t\u0305\u0306\n\u0007\u0000\u0000\u0306\u0307\u0005\u0015\u0000\u0000"+
		"\u0307\u032e\u0003~?\b\u0308\u0309\n\u0006\u0000\u0000\u0309\u030a\u0005"+
		"\u0014\u0000\u0000\u030a\u032e\u0003~?\u0007\u030b\u030c\n\u0005\u0000"+
		"\u0000\u030c\u030d\u0005\u0019\u0000\u0000\u030d\u032e\u0003~?\u0006\u030e"+
		"\u030f\n\u0004\u0000\u0000\u030f\u0310\u0005*\u0000\u0000\u0310\u032e"+
		"\u0003~?\u0005\u0311\u0312\n\u0003\u0000\u0000\u0312\u0313\u0005+\u0000"+
		"\u0000\u0313\u032e\u0003~?\u0004\u0314\u0315\n\u0002\u0000\u0000\u0315"+
		"\u0316\u0005\u001c\u0000\u0000\u0316\u0317\u0003~?\u0000\u0317\u0318\u0005"+
		"\r\u0000\u0000\u0318\u0319\u0003~?\u0003\u0319\u032e\u0001\u0000\u0000"+
		"\u0000\u031a\u031b\n\u0001\u0000\u0000\u031b\u031c\u0007\u0013\u0000\u0000"+
		"\u031c\u032e\u0003~?\u0001\u031d\u031e\n\u0019\u0000\u0000\u031e\u031f"+
		"\u0005\u0004\u0000\u0000\u031f\u032e\u0003\b\u0004\u0000\u0320\u0321\n"+
		"\u0018\u0000\u0000\u0321\u0322\u0005\u0007\u0000\u0000\u0322\u0323\u0003"+
		"~?\u0000\u0323\u0324\u0005\b\u0000\u0000\u0324\u032e\u0001\u0000\u0000"+
		"\u0000\u0325\u0326\n\u0017\u0000\u0000\u0326\u0328\u0005\u0002\u0000\u0000"+
		"\u0327\u0329\u0003\u0086C\u0000\u0328\u0327\u0001\u0000\u0000\u0000\u0328"+
		"\u0329\u0001\u0000\u0000\u0000\u0329\u032a\u0001\u0000\u0000\u0000\u032a"+
		"\u032e\u0005\u0003\u0000\u0000\u032b\u032c\n\u0014\u0000\u0000\u032c\u032e"+
		"\u0007\u0014\u0000\u0000\u032d\u02de\u0001\u0000\u0000\u0000\u032d\u02e1"+
		"\u0001\u0000\u0000\u0000\u032d\u02e4\u0001\u0000\u0000\u0000\u032d\u02e7"+
		"\u0001\u0000\u0000\u0000\u032d\u02ea\u0001\u0000\u0000\u0000\u032d\u02f5"+
		"\u0001\u0000\u0000\u0000\u032d\u02f8\u0001\u0000\u0000\u0000\u032d\u02fb"+
		"\u0001\u0000\u0000\u0000\u032d\u02ff\u0001\u0000\u0000\u0000\u032d\u0302"+
		"\u0001\u0000\u0000\u0000\u032d\u0305\u0001\u0000\u0000\u0000\u032d\u0308"+
		"\u0001\u0000\u0000\u0000\u032d\u030b\u0001\u0000\u0000\u0000\u032d\u030e"+
		"\u0001\u0000\u0000\u0000\u032d\u0311\u0001\u0000\u0000\u0000\u032d\u0314"+
		"\u0001\u0000\u0000\u0000\u032d\u031a\u0001\u0000\u0000\u0000\u032d\u031d"+
		"\u0001\u0000\u0000\u0000\u032d\u0320\u0001\u0000\u0000\u0000\u032d\u0325"+
		"\u0001\u0000\u0000\u0000\u032d\u032b\u0001\u0000\u0000\u0000\u032e\u0331"+
		"\u0001\u0000\u0000\u0000\u032f\u032d\u0001\u0000\u0000\u0000\u032f\u0330"+
		"\u0001\u0000\u0000\u0000\u0330\u007f\u0001\u0000\u0000\u0000\u0331\u032f"+
		"\u0001\u0000\u0000\u0000\u0332\u0337\u0003\u0084B\u0000\u0333\u0337\u0005"+
		"\u0087\u0000\u0000\u0334\u0337\u0003\u0010\b\u0000\u0335\u0337\u0003\b"+
		"\u0004\u0000\u0336\u0332\u0001\u0000\u0000\u0000\u0336\u0333\u0001\u0000"+
		"\u0000\u0000\u0336\u0334\u0001\u0000\u0000\u0000\u0336\u0335\u0001\u0000"+
		"\u0000\u0000\u0337\u0081\u0001\u0000\u0000\u0000\u0338\u033a\u0005\u0002"+
		"\u0000\u0000\u0339\u033b\u0003~?\u0000\u033a\u0339\u0001\u0000\u0000\u0000"+
		"\u033a\u033b\u0001\u0000\u0000\u0000\u033b\u0340\u0001\u0000\u0000\u0000"+
		"\u033c\u033d\u0005\u0006\u0000\u0000\u033d\u033f\u0003~?\u0000\u033e\u033c"+
		"\u0001\u0000\u0000\u0000\u033f\u0342\u0001\u0000\u0000\u0000\u0340\u033e"+
		"\u0001\u0000\u0000\u0000\u0340\u0341\u0001\u0000\u0000\u0000\u0341\u0343"+
		"\u0001\u0000\u0000\u0000\u0342\u0340\u0001\u0000\u0000\u0000\u0343\u0345"+
		"\u0005\u0003\u0000\u0000\u0344\u0338\u0001\u0000\u0000\u0000\u0344\u0345"+
		"\u0001\u0000\u0000\u0000\u0345\u0348\u0001\u0000\u0000\u0000\u0346\u0349"+
		"\u0003\b\u0004\u0000\u0347\u0349\u0003\u0012\t\u0000\u0348\u0346\u0001"+
		"\u0000\u0000\u0000\u0348\u0347\u0001\u0000\u0000\u0000\u0349\u0083\u0001"+
		"\u0000\u0000\u0000\u034a\u034b\u0005\u0002\u0000\u0000\u034b\u034c\u0003"+
		"~?\u0000\u034c\u034d\u0005\u0003\u0000\u0000\u034d\u0085\u0001\u0000\u0000"+
		"\u0000\u034e\u0350\u0005\u0006\u0000\u0000\u034f\u034e\u0001\u0000\u0000"+
		"\u0000\u034f\u0350\u0001\u0000\u0000\u0000\u0350\u0351\u0001\u0000\u0000"+
		"\u0000\u0351\u0358\u0003~?\u0000\u0352\u0354\u0005\u0006\u0000\u0000\u0353"+
		"\u0355\u0003~?\u0000\u0354\u0353\u0001\u0000\u0000\u0000\u0354\u0355\u0001"+
		"\u0000\u0000\u0000\u0355\u0357\u0001\u0000\u0000\u0000\u0356\u0352\u0001"+
		"\u0000\u0000\u0000\u0357\u035a\u0001\u0000\u0000\u0000\u0358\u0356\u0001"+
		"\u0000\u0000\u0000\u0358\u0359\u0001\u0000\u0000\u0000\u0359\u0087\u0001"+
		"\u0000\u0000\u0000\u035a\u0358\u0001\u0000\u0000\u0000\u035b\u035c\u0005"+
		"O\u0000\u0000\u035c\u0360\u0005\u000b\u0000\u0000\u035d\u035f\u0003\u008a"+
		"E\u0000\u035e\u035d\u0001\u0000\u0000\u0000\u035f\u0362\u0001\u0000\u0000"+
		"\u0000\u0360\u035e\u0001\u0000\u0000\u0000\u0360\u0361\u0001\u0000\u0000"+
		"\u0000\u0361\u0363\u0001\u0000\u0000\u0000\u0362\u0360\u0001\u0000\u0000"+
		"\u0000\u0363\u0364\u0005\f\u0000\u0000\u0364\u0089\u0001\u0000\u0000\u0000"+
		"\u0365\u0366\u0003\u008cF\u0000\u0366\u0367\u0005\u0005\u0000\u0000\u0367"+
		"\u0368\u0003\u0010\b\u0000\u0368\u008b\u0001\u0000\u0000\u0000\u0369\u0370"+
		"\u0003\b\u0004\u0000\u036a\u036b\u0005\u0002\u0000\u0000\u036b\u036c\u0005"+
		"<\u0000\u0000\u036c\u0371\u0005\u0003\u0000\u0000\u036d\u036e\u0005\u0007"+
		"\u0000\u0000\u036e\u036f\u0005<\u0000\u0000\u036f\u0371\u0005\b\u0000"+
		"\u0000\u0370\u036a\u0001\u0000\u0000\u0000\u0370\u036d\u0001\u0000\u0000"+
		"\u0000\u0370\u0371\u0001\u0000\u0000\u0000\u0371\u008d\u0001\u0000\u0000"+
		"\u0000\u0372\u0373\u0005H\u0000\u0000\u0373\u0374\u00059\u0000\u0000\u0374"+
		"\u0375\u0003\n\u0005\u0000\u0375\u0376\u00059\u0000\u0000\u0376\u0377"+
		"\u0005\u0004\u0000\u0000\u0377\u0378\u0005N\u0000\u0000\u0378\u0379\u0005"+
		"\u0004\u0000\u0000\u0379\u037a\u0003\b\u0004\u0000\u037a\u0385\u0001\u0000"+
		"\u0000\u0000\u037b\u037c\u0003\b\u0004\u0000\u037c\u037d\u0005\u0004\u0000"+
		"\u0000\u037d\u037f\u0001\u0000\u0000\u0000\u037e\u037b\u0001\u0000\u0000"+
		"\u0000\u037f\u0382\u0001\u0000\u0000\u0000\u0380\u037e\u0001\u0000\u0000"+
		"\u0000\u0380\u0381\u0001\u0000\u0000\u0000\u0381\u0383\u0001\u0000\u0000"+
		"\u0000\u0382\u0380\u0001\u0000\u0000\u0000\u0383\u0385\u0003\b\u0004\u0000"+
		"\u0384\u0372\u0001\u0000\u0000\u0000\u0384\u0380\u0001\u0000\u0000\u0000"+
		"\u0385\u008f\u0001\u0000\u0000\u0000\u0386\u038b\u0003\b\u0004\u0000\u0387"+
		"\u0388\u0005\u0006\u0000\u0000\u0388\u038a\u0003\b\u0004\u0000\u0389\u0387"+
		"\u0001\u0000\u0000\u0000\u038a\u038d\u0001\u0000\u0000\u0000\u038b\u0389"+
		"\u0001\u0000\u0000\u0000\u038b\u038c\u0001\u0000\u0000\u0000\u038c\u0091"+
		"\u0001\u0000\u0000\u0000\u038d\u038b\u0001\u0000\u0000\u0000]\u0096\u0098"+
		"\u009c\u00a2\u00a7\u00b9\u00c5\u00ce\u00d6\u00e8\u00f2\u00f7\u00fd\u0102"+
		"\u0106\u0111\u011c\u0125\u012e\u0134\u013d\u014a\u014e\u0154\u015a\u0167"+
		"\u016f\u017e\u0185\u0187\u018c\u0192\u0196\u019a\u01a0\u01a5\u01b1\u01bb"+
		"\u01c0\u01c7\u01cc\u01d1\u01da\u01dd\u01e4\u01e7\u01f0\u01f2\u01f9\u0201"+
		"\u0204\u0208\u021f\u0226\u0231\u0236\u023c\u0243\u0248\u024c\u0256\u025d"+
		"\u0261\u026f\u027a\u027f\u0285\u0289\u029c\u02ac\u02b0\u02bc\u02c3\u02c7"+
		"\u02d2\u02dc\u02f2\u0328\u032d\u032f\u0336\u033a\u0340\u0344\u0348\u034f"+
		"\u0354\u0358\u0360\u0370\u0380\u0384\u038b";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}