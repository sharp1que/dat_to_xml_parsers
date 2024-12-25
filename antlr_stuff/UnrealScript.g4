grammar UnrealScript;
program                  : classdecl
                           ( declarations | replicationblock | body)*
                           ( defaultpropertiesblock )?
                           ;

// CLASS
classdecl                : CLASS identifier ( EXTENDS packageidentifier )? ( classparams )* ';';
classparams              : constclassparams
                         | WITHIN packageidentifier
                         | DEPENDSON '(' packageidentifier ')'
                         | CONFIG ( '(' packageidentifier ')' )?
                         | HIDECATEGORIES '(' identifierlist ')'
                         | SHOWCATEGORIES '(' identifierlist ')';
constclassparams         : ABSTRACT
                         | NATIVE
                         | NATIVEREPLICATION
                         | NONATIVEREPLICATION
                         | SAFEREPLACE
                         | PEROBJECTCONFIG
                         | TRANSIENT
                         | NOEXPORT
                         | EXPORTSTRUCTS
                         | COLLAPSECATEGORIES
                         | DONTCOLLAPSECATEGORIES
                         | PLACEABLE
                         | NOTPLACEABLE
                         | EDITINLINENEW
                         | NOTEDITINLINENEW
                         | DYNAMICRECOMPILE;
identifier               : IDENT
                         | ABSTRACT
                         | ARRAY
                         | ASSERT
                         | AUTO
                         | BOOL
                         | BYTE
                         | CASE
                         | CLASS
                         | COERCE
                         | COLLAPSECATEGORIES
                         | CONFIG
                         | CONST
                         | CONSTRUCTIVE
                         | DEFAULT
                         | DEFAULTPROPERTIES
                         | DELEGATE
                         | DEPENDSON
                         | DEPRECATED
                         | DO
                         | DONTCOLLAPSECATEGORIES
                         | DYNAMICRECOMPILE
                         | EDFINDABLE
                         | EDITCONST
                         | EDITINLINE
                         | EDITINLINENEW
                         | EDITINLINENOTIFY
                         | EDITINLINEUSE
                         | ELSE
                         | ENUM
                         | EVENT
                         | EXEC
                         | EXPORT
                         | EXPORTSTRUCTS
                         | EXTENDS
                         | FINAL
                         | FLOAT
                         | FOR
                         | FOREACH
                         | FUNCTION
                         | GLOBALCONFIG
                         | HIDECATEGORIES
                         | IF
                         | IGNORES
                         | INPUT
                         | INT
                         | ITERATOR
                         | LATENT
                         | LOCAL
                         | LOCALIZED
                         | NAME
                         | NATIVE
                         | NATIVEREPLICATION
                         | NEW
                         | NOEXPORT
                         | NONATIVEREPLICATION
                         | NOTEDITINLINENEW
                         | NOTPLACEABLE
                         | OPERATOR
                         | OPTIONAL
                         | OUT
                         | PEROBJECTCONFIG
                         | PLACEABLE
                         | POSTOPERATOR
                         | PREOPERATOR
                         | PRIVATE
                         | PROTECTED
                         | RELIABLE
                         | REPLICATION
                         | RETURN
                         | SAFEREPLACE
                         | SELF
                         | SHOWCATEGORIES
                         | SIMULATED
                         | SINGULAR
                         | SKIP_
                         | STATE
                         | STATIC
                         | STRING
                         | STRUCT
                         | SWITCH
                         | TRANSIENT
                         | TRAVEL
                         | UNRELIABLE
                         | UNTIL
                         | VAR
                         | WHILE
                         | WITHIN;
packageidentifier        : ( identifier '.' )? identifier;

// DECLARATIONS
declarations             : ( constdecl | vardecl | enumdecl | structdecl ) ';';

constdecl                : CONST identifier '=' expression;
constvalue               : ( StringVal | NameVal | IntVal | FloatVal | BoolVal | NoneVal | classval | objectval | VectVal);
classval                 : CLASS NameVal;
objectval                : identifier NameVal;

vardecl                  : VAR ( configgroup )? ( varparams )* vartype varidentifier arrayindex? ( ',' varidentifier arrayindex? )*;
arrayindex               : ('[' expression ']');
varparams                : CONFIG | CONST | EDITCONST | EXPORT | GLOBALCONFIG | INPUT |
                           LOCALIZED | NATIVE | PRIVATE | PROTECTED | TRANSIENT | TRAVEL |
                           EDITINLINE | DEPRECATED | EDFINDABLE | EDITINLINEUSE | EDITINLINENOTIFY;
configgroup              : '(' ( identifier )? ')';
vartype                  : arraydecl | dynarraydecl | packageidentifier | enumdecl | structdecl | classtype | basictype;
basictype                : BYTE | INT | FLOAT | STRING | BOOL | NAME;
varidentifier            : identifier;

arraydecl                : identifier '[' expression? ']';
dynarraydecl             : ARRAY '<' ( varparams )* (packageidentifier | classtype | basictype) '>';
classtype                : CLASS ('<' packageidentifier '>')?;

enumdecl                 : ENUM identifier '{' enumoptions '}';
enumoptions              : identifier ( ',' identifier )* ','?;

structdecl               : STRUCT ( structparams )* identifier ( EXTENDS packageidentifier )?
                           '{' structbody '}';
structparams             : ( NATIVE | EXPORT | CONSTRUCTIVE);
structbody               : ( vardecl ';' )*;


// REPLICATION
replicationblock         : REPLICATION '{' ( replicationbody )* '}';
replicationbody          : ( RELIABLE | UNRELIABLE ) IF '(' expression ')'
                           identifier ( ',' identifier )* ';';

// BODY
body                     : ( statedecl | functiondecl )+;

// State parts
statedecl                : ( stateparams )* STATE ('(' ')')? identifier ( configgroup )? ( EXTENDS identifier )? statebody;
statebody                : '{' ( stateignore )? ( functiondecl )* statelabels '}';
stateignore              : IGNORES identifier ( ',' identifier )* ';';
statelabels              : ( identifier ':' ( statement )* )*;
stateparams              : AUTO | SIMULATED;

// Function parts
functiondecl             : ( normalfunc | operatorfunc );

normalfunc               : ( functionparams )* functiontype ( localtype )?
                           identifier '(' ( functionargs ( ',' functionargs )* )? ')'
                           ('{' functionbody '}')? ';'?;
functiontype             : FUNCTION | EVENT | DELEGATE;

functionparams           : constfuncparams | NATIVE ( '(' IntVal ')' )?;
constfuncparams          : FINAL | ITERATOR | LATENT | SIMULATED | SINGULAR | STATIC |
                           EXEC | PROTECTED | PRIVATE;

operatorfunc             : ( functionparams )* operatortype ('{' functionbody '}')? ';'?;
operatortype             : ( binaryoperator | unaryoperator );
binaryoperator           : OPERATOR '(' IntVal ')' localtype opidentifier
                           '(' functionargs ',' functionargs ')'  ;
unaryoperator            : ( PREOPERATOR | POSTOPERATOR ) localtype opidentifier
                           '(' functionargs ')' ;
opidentifier             : identifier | operatornames;
operatornames            : '~' | '!' | '@' | '#' | '$' | '%' | '^' | '&' | '*' |
                           '-' | '=' | '+' | '|' | '\\' | ':' | '<' | '>' | '/' |
                           '?' | '`' |
                           '<<' | '>>' | '!=' | '<=' | '>=' | '++' | '--' | '?-' | '+=' |
                           '-=' | '*=' | '/=' | '&&' | '||' | '^^' | '==' | '**' |
                           '~=' | '@=' | '>>>';

functionargs             : ( OPTIONAL | OUT | COERCE | SKIP_ )* functionargtype identifier;
functionargtype          : arraydecl | dynarraydecl | packageidentifier | classtype | basictype;
functionbody             : ( localdecl )* ( statement )*;
localdecl                : LOCAL localtype identifier arrayindex? ( ',' identifier arrayindex? )* ';';
localtype                : packageidentifier | arraydecl | dynarraydecl | classtype | basictype;

// Code parts
codeblock                : ( statement | ( '{' ( statement )* '}' ) );

statement                : ';'
                         | assertion
                         | ifstatement
                         | switchstatement
                         | whileloop
                         | doloop
                         | foreachloop
                         | forloop
                         | returnstatement
                         | expression ';';
assertion                : ASSERT expression ';';
ifstatement              : IF parExpression codeblock ( ELSE codeblock )?;
switchstatement          : SWITCH (parExpression | expression) '{' ( caserule )* ( defaultrule )? '}';
whileloop                : WHILE parExpression codeblock;
doloop                   : DO codeblock UNTIL '(' expression ')';
foreachloop              : FOREACH qualifiedidentifier '(' expressionList? ')' codeblock;
forloop                  : FOR '(' identifier '=' expression ';' expression ';' expression ')' codeblock?;
returnstatement          : RETURN ( expression )? ';';

caserule                 : CASE expression ':' casecodeblock;
casecodeblock            : statement* | ( '{' statement* '}' );
defaultrule              : DEFAULT ':' casecodeblock;

expression               : primary
                         |   expression '.' identifier
                         |   expression '[' expression ']'
                         |   expression '(' expressionList? ')'
                         |   basictype '(' expressionList? ')'
                         |   NEW creator
                         |   expression ('++' | '--')
                         |   ('+'|'-'|'++'|'--') expression
                         |   ('~'|'!') expression
                         |   expression ('*'|'/'|'%') expression
                         |   expression ('+'|'-') expression
                         |   expression '^^' expression
                         |   expression ('>>' | '<<' | '>>>') expression
                         |   expression ('<' '<' | '>' '>' '>' | '>' '>') expression
                         |   expression ('<=' | '>=' | '>' | '<') expression
                         |   expression ('==' | '!=') expression
                         |   expression identifier expression
                         |   expression '@' expression
                         |   expression '$' expression
                         |   expression '&' expression
                         |   expression '^' expression
                         |   expression '|' expression
                         |   expression '&&' expression
                         |   expression '||' expression
                         |   expression '?' expression ':' expression
                         |   <assoc=right> expression
                             (   '='
                             |   '+='
                             |   '-='
                             |   '*='
                             |   '/='
                             |   '&='
                             |   '|='
                             |   '^='
                             |   '>>='
                             |   '>>>='
                             |   '<<='
                             |   '%='
                             |   '~='
                             )
                             expression;
primary                  : parExpression | SELF | constvalue | identifier;
creator                  : ('(' expression? (',' expression)*')')? (identifier | classval);
parExpression            : '(' expression ')';
expressionList           : ','? expression (',' expression?)*;

// DEFAULTPROPERTIES
defaultpropertiesblock   : DEFAULTPROPERTIES '{' ( defprop )* '}';
defprop                  : defpropidentifier '=' constvalue;
defpropidentifier        : identifier ( ( '(' IntVal ')' ) | ( '[' IntVal ']' ) )?;


qualifiedidentifier      : ( ( CLASS '\'' packageidentifier '\'' '.' DEFAULT '.' identifier )
                           | ( ( identifier '.' )* identifier )
                           );
identifierlist           : identifier ( ',' identifier )*;

// LITERALS
StringVal                : '"' StringCharacters? '"';
NameVal                  : '\'' NameCharacters? '\'';
IntVal                   : (DecimalIntegerLiteral | HexIntegerLiteral);
FloatVal                 : (Digits '.' Digits? ExponentPart? | Digits ExponentPart | Digits) F?;
BoolVal                  : (F A L S E) | (T R U E);
NoneVal                  : N O N E;
VectVal                  : V E C T '(' FloatVal ',' FloatVal ',' FloatVal ')';

// KEYWORDS
ABSTRACT: A B S T R A C T;
ARRAY: A R R A Y;
ASSERT: A S S E R T;
AUTO: A U T O;
BOOL: B O O L;
BYTE: B Y T E;
CASE: C A S E;
CLASS: C L A S S;
COERCE: C O E R C E;
COLLAPSECATEGORIES: C O L L A P S E C A T E G O R I E S;
CONFIG: C O N F I G;
CONST: C O N S T;
CONSTRUCTIVE: C O N S T R U C T I V E;
DEFAULT: D E F A U L T;
DEFAULTPROPERTIES: D E F A U L T P R O P E R T I E S;
DELEGATE: D E L E G A T E;
DEPENDSON: D E P E N D S O N;
DEPRECATED: D E P R E C A T E D;
DO: D O;
DONTCOLLAPSECATEGORIES: D O N T C O L L A P S E C A T E G O R I E S;
DYNAMICRECOMPILE: D Y N A M I C R E C O M P I L E;
EDFINDABLE: E D F I N D A B L E;
EDITCONST: E D I T C O N S T;
EDITINLINE: E D I T I N L I N E;
EDITINLINENEW: E D I T I N L I N E N E W;
EDITINLINENOTIFY: E D I T I N L I N E N O T I F Y;
EDITINLINEUSE: E D I T I N L I N E U S E;
ELSE: E L S E;
ENUM: E N U M;
EVENT: E V E N T;
EXEC: E X E C;
EXPORT: E X P O R T;
EXPORTSTRUCTS: E X P O R T S T R U C T S;
EXTENDS: E X T E N D S;
FINAL: F I N A L;
FLOAT: F L O A T;
FOR: F O R;
FOREACH: F O R E A C H;
FUNCTION: F U N C T I O N;
GLOBALCONFIG: G L O B A L C O N F I G;
HIDECATEGORIES: H I D E C A T E G O R I E S;
IF: I F;
IGNORES: I G N O R E S;
INPUT: I N P U T;
INT: I N T;
ITERATOR: I T E R A T O R;
LATENT: L A T E N T;
LOCAL: L O C A L;
LOCALIZED: L O C A L I Z E D;
NAME: N A M E;
NATIVE: N A T I V E;
NATIVEREPLICATION: N A T I V E R E P L I C A T I O N;
NEW: N E W;
NOEXPORT: N O E X P O R T;
NONATIVEREPLICATION: N O N A T I V E R E P L I C A T I O N;
NOTEDITINLINENEW: N O T E D I T I N L I N E N E W;
NOTPLACEABLE: N O T P L A C E A B L E;
OPERATOR: O P E R A T O R;
OPTIONAL: O P T I O N A L;
OUT: O U T;
PEROBJECTCONFIG: P E R O B J E C T C O N F I G;
PLACEABLE: P L A C E A B L E;
POSTOPERATOR: P O S T O P E R A T O R;
PREOPERATOR: P R E O P E R A T O R;
PRIVATE: P R I V A T E;
PROTECTED: P R O T E C T E D;
RELIABLE: R E L I A B L E;
REPLICATION: R E P L I C A T I O N;
RETURN: R E T U R N;
SAFEREPLACE: S A F E R E P L A C E;
SELF: S E L F;
SHOWCATEGORIES: S H O W C A T E G O R I E S;
SIMULATED: S I M U L A T E D;
SINGULAR: S I N G U L A R;
SKIP_: S K I P;
STATE: S T A T E;
STATIC: S T A T I C;
STRING: S T R I G N;
STRUCT: S T R U C T;
SWITCH: S W I T C H;
TRANSIENT: T R A N S I E N T;
TRAVEL: T R A V E L;
UNRELIABLE: U N R E L I A B L E;
UNTIL: U N T I L;
VAR: V A R;
WHILE: W H I L E;
WITHIN: W I T H I N;

fragment Alpha           : [a-zA-Z_];
fragment StringCharacters: StringCharacter+;
fragment StringCharacter : EscapeSequence | ~["\\];
fragment EscapeSequence  : '\\' [nt"\\];
fragment NameCharacters  : NameCharacter+;
fragment NameCharacter   : ~['];
fragment DecimalIntegerLiteral : '0' | NonZeroDigit Digits?;
fragment HexIntegerLiteral : '0' [xX] HexDigits;
fragment Digits          : Digit+;
fragment Digit           : '0' | NonZeroDigit;
fragment NonZeroDigit    : [1-9];
fragment HexDigits       : HexDigit+;
fragment HexDigit        : [0-9a-fA-F];
fragment ExponentPart    : ExponentIndicator SignedInteger;
fragment ExponentIndicator : [eE];
fragment SignedInteger   : Sign? Digits;
fragment Sign            : [+-];

fragment A: [aA];
fragment B: [bB];
fragment C: [cC];
fragment D: [dD];
fragment E: [eE];
fragment F: [fF];
fragment G: [gG];
fragment H: [hH];
fragment I: [iI];
fragment J: [jJ];
fragment K: [kK];
fragment L: [lL];
fragment M: [mM];
fragment N: [nN];
fragment O: [oO];
fragment P: [pP];
fragment Q: [qQ];
fragment R: [rR];
fragment S: [sS];
fragment T: [tT];
fragment U: [uU];
fragment V: [vV];
fragment W: [wW];
fragment X: [xX];
fragment Y: [yY];
fragment Z: [zZ];

IDENT                    : [a-zA-Z_] [a-zA-Z0-9_]*;

// Whitespaces and comments
WS                       : [ \t\r\n\u000C]+ -> skip;
DIRECTIVE                : '#' ~[\r\n]* -> skip;
COMMENT                  : '/*' (COMMENT|.)*? '*/' -> skip;
LINE_COMMENT             : '//' ~[\r\n]* -> skip;